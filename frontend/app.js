/**
 * DocSyntax AI - Client-side UI Controller & Backend Connector
 * Connects the 3-panel UI with the FastAPI & Qdrant RAG Backend.
 * Features:
 * - Real-time query submission to /api/query
 * - Supported technologies modal from /api/technologies
 * - Dark & Light mode toggle
 * - Safe fallback if backend is offline
 */

document.addEventListener("DOMContentLoaded", () => {
  // DOM Elements
  const themeToggle = document.getElementById("themeToggle");
  const themeLabel = document.getElementById("themeLabel");
  const promptForm = document.getElementById("promptForm");
  const promptInput = document.getElementById("promptInput");
  const clearBtn = document.getElementById("clearBtn");
  const copyBtn = document.getElementById("copyBtn");
  const submitBtn = document.getElementById("submitBtn");
  const exampleChips = document.querySelectorAll(".example-chip");

  // Modal elements
  const techListBtn = document.getElementById("techListBtn");
  const techModal = document.getElementById("techModal");
  const closeModalBtn = document.getElementById("closeModalBtn");
  const techModalBody = document.getElementById("techModalBody");
  const techSearchInput = document.getElementById("techSearchInput");

  // Explanation elements
  const explanationEmpty = document.getElementById("explanationEmpty");
  const explanationBody = document.getElementById("explanationBody");
  const sourceBadge = document.getElementById("sourceBadge");

  // Syntax elements
  const syntaxEmpty = document.getElementById("syntaxEmpty");
  const syntaxBody = document.getElementById("syntaxBody");
  const syntaxPanel = document.getElementById("syntaxPanel");

  // Backend API URL:
  // When served by FastAPI (production deployment on Render/Railway/cloud, or local on port 8000), use relative path "" (same origin).
  // When opened via file:// or separate frontend dev server (e.g. Live Server on port 5500), fall back to http://127.0.0.1:8000.
  const isSeparatedDevClient = window.location.protocol === "file:" || 
    ((window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1") && window.location.port !== "8000" && window.location.port !== "");
  const API_BASE = isSeparatedDevClient ? "http://127.0.0.1:8000" : "";

  let allCategoriesData = [];

  // ---------------------------------------------------------------------------
  // 1. THEME TOGGLE (DARK / LIGHT MODE)
  // ---------------------------------------------------------------------------
  const savedTheme = localStorage.getItem("docsyntax_theme") || "dark";
  applyTheme(savedTheme);

  themeToggle.addEventListener("click", () => {
    const currentTheme = document.documentElement.getAttribute("data-theme") || "dark";
    const nextTheme = currentTheme === "dark" ? "light" : "dark";
    applyTheme(nextTheme);
  });

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("docsyntax_theme", theme);
    themeLabel.textContent = theme === "dark" ? "Dark" : "Light";
  }

  // ---------------------------------------------------------------------------
  // 2. SUPPORTED TECHNOLOGIES MODAL
  // ---------------------------------------------------------------------------
  techListBtn.addEventListener("click", openTechModal);
  closeModalBtn.addEventListener("click", closeTechModal);
  techModal.addEventListener("click", (e) => {
    if (e.target === techModal) closeTechModal();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && techModal.style.display !== "none") {
      closeTechModal();
    }
  });

  function openTechModal() {
    techModal.style.display = "flex";
    techSearchInput.value = "";
    techSearchInput.focus();
    loadTechnologies();
  }

  function closeTechModal() {
    techModal.style.display = "none";
  }

  async function loadTechnologies() {
    if (allCategoriesData.length > 0) {
      renderTechModal(allCategoriesData);
      return;
    }

    try {
      const resp = await fetch(`${API_BASE}/api/technologies`);
      if (resp.ok) {
        const data = await resp.json();
        allCategoriesData = data.categories || [];
        renderTechModal(allCategoriesData);
        techListBtn.querySelector("span").textContent = `Indexed Technologies (${data.total_technologies || 24})`;
        return;
      }
    } catch (err) {
      console.log("Using cached technology list.");
    }

    // Static fallback if API is not yet loaded
    allCategoriesData = [
      {
        category: "Languages",
        technologies: [
          { name: "Python", documents_count: 14 },
          { name: "JavaScript", documents_count: 100 },
          { name: "TypeScript", documents_count: 25 },
          { name: "C", documents_count: 21 },
          { name: "C++", documents_count: 23 },
          { name: "SQL", documents_count: 75 }
        ]
      },
      {
        category: "Backend & APIs",
        technologies: [
          { name: "FastAPI", documents_count: 100 },
          { name: "Express.js", documents_count: 16 },
          { name: "Node.js", documents_count: 99 },
          { name: "Prisma ORM", documents_count: 100 },
          { name: "JWT", documents_count: 91 },
          { name: "Socket.IO", documents_count: 50 },
          { name: "REST APIs", documents_count: 50 }
        ]
      },
      {
        category: "Frontend",
        technologies: [
          { name: "React.js", documents_count: 40 },
          { name: "Streamlit", documents_count: 100 },
          { name: "TailwindCSS", documents_count: 25 },
          { name: "Vite", documents_count: 20 },
          { name: "HTML5", documents_count: 50 },
          { name: "CSS3", documents_count: 50 }
        ]
      },
      {
        category: "ML & Data",
        technologies: [
          { name: "pandas", documents_count: 35 },
          { name: "NumPy", documents_count: 51 },
          { name: "LLMs", documents_count: 67 },
          { name: "RAG", documents_count: 26 },
          { name: "XGBoost", documents_count: 21 },
          { name: "SHAP", documents_count: 3 },
          { name: "scikit-learn", documents_count: 1 }
        ]
      },
      {
        category: "Core Concepts",
        technologies: [
          { name: "Data Structures & Algorithms", documents_count: 24 },
          { name: "OOP", documents_count: 9 },
          { name: "DBMS", documents_count: 15 },
          { name: "Operating Systems", documents_count: 15 }
        ]
      }
    ];

    renderTechModal(allCategoriesData);
  }

  function renderTechModal(categories) {
    const filter = techSearchInput.value.trim().toLowerCase();
    let html = "";

    categories.forEach(cat => {
      const filteredTechs = cat.technologies.filter(t => 
        !filter || t.name.toLowerCase().includes(filter) || cat.category.toLowerCase().includes(filter)
      );

      if (filteredTechs.length > 0) {
        html += `
          <div class="modal-category">
            <span class="modal-category-title">${escapeHtml(cat.category)}</span>
            <div class="tech-grid">
              ${filteredTechs.map(t => `
                <div class="tech-badge-item" data-tech="${escapeHtml(t.name)}">
                  <span>${escapeHtml(t.name)}</span>
                  ${t.documents_count ? `<span class="tech-badge-count">(${t.documents_count} docs)</span>` : ""}
                </div>
              `).join("")}
            </div>
          </div>
        `;
      }
    });

    techModalBody.innerHTML = html || `<p class="empty-desc" style="text-align: center; padding: 20px;">No technologies matching "${escapeHtml(filter)}"</p>`;

    // Add click event to insert filter into prompt
    techModalBody.querySelectorAll(".tech-badge-item").forEach(badge => {
      badge.addEventListener("click", () => {
        const tech = badge.dataset.tech;
        promptInput.value = `[${tech}] `;
        closeTechModal();
        promptInput.focus();
      });
    });
  }

  techSearchInput.addEventListener("input", () => {
    renderTechModal(allCategoriesData);
  });

  // ---------------------------------------------------------------------------
  // 3. BACKEND QUERY SUBMISSION
  // ---------------------------------------------------------------------------
  promptForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleSubmit();
  });

  promptInput.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault();
      handleSubmit();
    }
  });

  async function handleSubmit() {
    const rawQuery = promptInput.value.trim();
    if (!rawQuery) return;

    // Check for [Tech] prefix
    let techFilter = null;
    let query = rawQuery;

    if (rawQuery.startsWith("[") && rawQuery.includes("]")) {
      const parts = rawQuery.split("]");
      techFilter = parts[0].replace("[", "").trim();
      query = parts.slice(1).join("]").trim();
    }

    setLoadingState(true);

    try {
      // 1. Try real backend call
      const response = await fetch(`${API_BASE}/api/query`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query, technology: techFilter })
      });

      if (response.ok) {
        const data = await response.json();
        renderBackendResult(data);
        setLoadingState(false);
        return;
      }
    } catch (err) {
      console.log("Backend offline, falling back to local client preview: ", err);
    }

    // 2. Client fallback preview if server is not active
    setTimeout(() => {
      handleClientMock(query, techFilter);
      setLoadingState(false);
    }, 400);
  }

  function setLoadingState(isLoading) {
    if (isLoading) {
      submitBtn.disabled = true;
      submitBtn.querySelector("span").textContent = "Searching Docs...";
      
      explanationEmpty.style.display = "none";
      explanationBody.style.display = "flex";
      explanationBody.innerHTML = `
        <div class="empty-state" style="padding: 40px 20px;">
          <div class="empty-illustration">
            <svg class="spin-icon" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10" stroke-opacity="0.25"></circle>
              <path d="M12 2a10 10 0 0 1 10 10"></path>
            </svg>
          </div>
          <p class="empty-title">Searching Official Documentation</p>
          <p class="empty-desc">Retrieving semantic context from Qdrant and generating code syntax...</p>
        </div>
      `;

      syntaxEmpty.style.display = "none";
      syntaxBody.style.display = "flex";
      copyBtn.style.display = "none";
      syntaxBody.innerHTML = `
        <div class="empty-state" style="padding: 40px 20px;">
          <p class="empty-title">Generating Syntax Solution</p>
          <p class="empty-desc">Formatting copy-pasteable code and parameter breakdowns...</p>
        </div>
      `;
    } else {
      submitBtn.disabled = false;
      submitBtn.querySelector("span").textContent = "Generate Syntax";
    }
  }

  // ---------------------------------------------------------------------------
  // 4. RENDER BACKEND API RESPONSE
  // ---------------------------------------------------------------------------
  function renderBackendResult(data) {
    // 1. Out of Bounds Check
    if (data.is_out_of_bounds) {
      sourceBadge.textContent = "Out of Bounds";
      sourceBadge.style.display = "inline-block";
      sourceBadge.style.borderColor = "var(--border-prominent)";

      explanationEmpty.style.display = "none";
      explanationBody.style.display = "flex";
      explanationBody.innerHTML = `
        <div class="content-section">
          <span class="section-label" style="color: var(--accent-amber);">Scope Policy Notification</span>
          <p class="concept-text" style="font-weight: 500;">
            ${escapeHtml(data.concept || data.raw_answer)}
          </p>
        </div>
        <div class="content-section" style="margin-top: 10px;">
          <p class="concept-text" style="color: var(--text-secondary); font-size: 0.85rem;">
            This system strictly limits answers to the 24+ technologies indexed in the knowledge base (e.g. Python, FastAPI, React, pandas, SQL, etc.). Click <strong>"Indexed Technologies"</strong> above to see supported topics.
          </p>
        </div>
      `;

      syntaxEmpty.style.display = "flex";
      syntaxBody.style.display = "none";
      copyBtn.style.display = "none";
      return;
    }

    // 2. In-Bounds Documentation Response
    const techName = data.technology || (data.sources && data.sources[0]?.technology) || "Documentation";
    sourceBadge.textContent = `${techName} Docs`;
    sourceBadge.style.display = "inline-block";
    sourceBadge.style.borderColor = "rgba(71, 104, 93, 0.25)";

    // Top-Left Panel: Explanation & Why to Use
    explanationEmpty.style.display = "none";
    explanationBody.style.display = "flex";

    const whyItems = data.why_to_use && data.why_to_use.length > 0
      ? data.why_to_use.map(item => `
          <li class="feature-item">
            <span class="feature-bullet">•</span>
            <span>${formatSimpleText(item)}</span>
          </li>
        `).join("")
      : `<li class="feature-item"><span class="feature-bullet">•</span><span>Provides officially documented syntax and standard implementation.</span></li>`;

    const sourcesHtml = data.sources && data.sources.length > 0
      ? data.sources.map(s => `
          <div class="doc-source-card">
            <span>Source:</span>
            <a href="${escapeHtml(s.source_url || '#')}" target="_blank" rel="noopener noreferrer">
              ${escapeHtml(s.breadcrumb || s.title || s.technology)} ↗
            </a>
          </div>
        `).join("")
      : "";

    explanationBody.innerHTML = `
      <div class="content-section">
        <span class="section-label">Explanation & Concept</span>
        <div class="concept-text" style="white-space: pre-line;">${formatSimpleText(data.concept || "")}</div>
      </div>

      <div class="content-section">
        <span class="section-label">Why Use This Approach</span>
        <ul class="feature-list">${whyItems}</ul>
      </div>

      ${data.caveats ? `
        <div class="content-section">
          <span class="section-label">Important Caveats & Gotchas</span>
          <div class="concept-text" style="color: var(--text-secondary); font-size: 0.85rem; white-space: pre-line;">
            ${formatSimpleText(data.caveats)}
          </div>
        </div>
      ` : ""}

      ${sourcesHtml}
    `;

    // Right Column: Syntax with Code
    if (data.code) {
      syntaxEmpty.style.display = "none";
      syntaxBody.style.display = "flex";
      copyBtn.style.display = "flex";

      const syntaxCards = data.syntax_breakdown && data.syntax_breakdown.length > 0
        ? data.syntax_breakdown.map(p => `
            <div class="param-card">
              <span class="param-name">${escapeHtml(p.name)}</span>
              <span class="param-desc">${escapeHtml(p.desc)}</span>
            </div>
          `).join("")
        : "";

      syntaxBody.innerHTML = `
        <div class="code-wrapper">
          <div class="code-header-bar">
            <span class="code-lang-tag">${escapeHtml(data.language || "code")}</span>
            <span>Official syntax implementation</span>
          </div>
          <pre class="code-pre"><code>${escapeHtml(data.code)}</code></pre>
        </div>

        ${syntaxCards ? `
          <div class="content-section" style="margin-top: 10px;">
            <span class="section-label">Syntax & Parameter Breakdown</span>
            <div class="syntax-breakdown">${syntaxCards}</div>
          </div>
        ` : ""}
      `;

      syntaxPanel.dataset.rawCode = data.code;
    } else {
      // In case LLM returned raw text
      syntaxEmpty.style.display = "none";
      syntaxBody.style.display = "flex";
      syntaxBody.innerHTML = `<div class="concept-text" style="white-space: pre-line;">${escapeHtml(data.raw_answer)}</div>`;
      copyBtn.style.display = "none";
    }
  }

  // ---------------------------------------------------------------------------
  // 5. CLIENT FALLBACK MOCK (FOR PREVIEW)
  // ---------------------------------------------------------------------------
  function handleClientMock(query, techFilter) {
    const q = query.toLowerCase();

    // Check Out of bounds
    if (q.includes("rust") || q.includes("mongo") || q.includes("binary search") || q.includes("weather") || q.includes("capital")) {
      renderBackendResult({
        is_out_of_bounds: true,
        concept: "This topic is outside the scope of the indexed documentation. The knowledge base does not contain official documentation for this query. I can only assist with technologies, syntax, and concepts available in the indexed documentation."
      });
      return;
    }

    // Default mock response
    renderBackendResult({
      technology: techFilter || "pandas",
      is_out_of_bounds: false,
      code: `import pandas as pd\n\n# Sample DataFrame\ndf = pd.DataFrame({\n    "product": ["A", "B", "C"],\n    "value": [10, 25, 30]\n})\n\n# Filter rows where value > 15\nfiltered_df = df[df["value"] > 15]\nprint(filtered_df)`,
      language: "python",
      concept: "Boolean indexing in pandas creates an aligned Series of True/False flags for each row. The DataFrame extracts only the rows matching True without modifying the original data.",
      why_to_use: [
        "Highly vectorized C/Cython execution speed.",
        "Readable and idiomatic standard syntax.",
        "Safely handles multi-criteria masks using & and |."
      ],
      caveats: "Wrap each separate condition in parentheses when combining with & or |. Otherwise operator precedence will raise a ValueError.",
      syntax_breakdown: [
        { name: "df[mask]", desc: "Filters rows using a boolean Series." },
        { name: "df.query(expr)", desc: "String-based query alternative." }
      ],
      sources: [
        { title: "Indexing and Selecting Data", source_url: "https://pandas.pydata.org/docs/user_guide/indexing.html", technology: "pandas" }
      ]
    });
  }

  // ---------------------------------------------------------------------------
  // 6. QUICK EXAMPLE CHIPS
  // ---------------------------------------------------------------------------
  exampleChips.forEach(chip => {
    chip.addEventListener("click", () => {
      promptInput.value = chip.dataset.query;
      promptInput.focus();
      handleSubmit();
    });
  });

  // ---------------------------------------------------------------------------
  // 7. CLEAR ACTION
  // ---------------------------------------------------------------------------
  clearBtn.addEventListener("click", () => {
    promptInput.value = "";
    promptInput.focus();
    explanationEmpty.style.display = "flex";
    explanationBody.style.display = "none";
    sourceBadge.style.display = "none";
    syntaxEmpty.style.display = "flex";
    syntaxBody.style.display = "none";
    copyBtn.style.display = "none";
  });

  // ---------------------------------------------------------------------------
  // 8. COPY CODE ACTION
  // ---------------------------------------------------------------------------
  copyBtn.addEventListener("click", async () => {
    const code = syntaxPanel.dataset.rawCode || "";
    if (!code) return;

    try {
      await navigator.clipboard.writeText(code);
      const btnText = copyBtn.querySelector(".btn-text");
      const orig = btnText.textContent;
      btnText.textContent = "Copied!";
      copyBtn.classList.add("copied");
      setTimeout(() => {
        btnText.textContent = orig;
        copyBtn.classList.remove("copied");
      }, 2000);
    } catch (err) {
      console.error("Clipboard copy failed: ", err);
    }
  });

  function escapeHtml(text) {
    if (!text) return "";
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }

  function formatSimpleText(text) {
    if (!text) return "";
    let safe = escapeHtml(text);
    // Convert `code` to <code class="inline-code">code</code>
    safe = safe.replace(/`([^`\n]+)`/g, '<code class="inline-code">$1</code>');
    // Convert **bold** to <strong>bold</strong>
    safe = safe.replace(/\*\*([^*\n]+)\*\*/g, '<strong>$1</strong>');
    return safe;
  }

  // Pre-load technology list
  loadTechnologies();
});

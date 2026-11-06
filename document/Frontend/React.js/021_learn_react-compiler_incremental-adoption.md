---
id: "react.js_021"
technology: "React.js"
category: "Frontend"
title: "Incremental Adoption – React"
doc_order: 21
source_url: "https://react.dev/learn/react-compiler/incremental-adoption"
language: "en"
retrieved_at: "2026-11-03 17:58:37"
content_hash: "11947ab6bab9a3dc0993ecb2b12069b0923afb9de1c63ba8af01545724abfddc"
---

# Incremental Adoption – React

Source: https://react.dev/learn/react-compiler/incremental-adoption

---

React Compiler can be adopted incrementally, allowing you to try it on specific parts of your codebase first. This guide shows you how to gradually roll out the compiler in existing projects.

### You will learn

- Why incremental adoption is recommended
- Using Babel overrides for directory-based adoption
- Using the “use memo” directive for opt-in compilation
- Using the “use no memo” directive to exclude components
- Runtime feature flags with gating
- Monitoring your adoption progress

React Compiler is designed to optimize your entire codebase automatically, but you don’t have to adopt it all at once. Incremental adoption gives you control over the rollout process, letting you test the compiler on small parts of your app before expanding to the rest.

Starting small helps you build confidence in the compiler’s optimizations. You can verify that your app behaves correctly with compiled code, measure performance improvements, and identify any edge cases specific to your codebase. This approach is especially valuable for production applications where stability is critical.

Incremental adoption also makes it easier to address any Rules of React violations the compiler might find. Instead of fixing violations across your entire codebase at once, you can tackle them systematically as you expand compiler coverage. This keeps the migration manageable and reduces the risk of introducing bugs.

By controlling which parts of your code get compiled, you can also run A/B tests to measure the real-world impact of the compiler’s optimizations. This data helps you make informed decisions about full adoption and demonstrates the value to your team.

There are three main approaches to adopt React Compiler incrementally:

1. **Babel overrides** - Apply the compiler to specific directories
2. **Opt-in with “use memo”** - Only compile components that explicitly opt in
3. **Runtime gating** - Control compilation with feature flags

All approaches allow you to test the compiler on specific parts of your application before full rollout.

Babel’s `overrides` option lets you apply different plugins to different parts of your codebase. This is ideal for gradually adopting React Compiler directory by directory.

Start by applying the compiler to a specific directory:

```
// babel.config.js
module.exports = {
  plugins: [
    // Global plugins that apply to all files
  ],
  overrides: [
    {
      test: './src/modern/**/*.{js,jsx,ts,tsx}',
      plugins: [
        'babel-plugin-react-compiler'
      ]
    }
  ]
};
```
As you gain confidence, add more directories:

```
// babel.config.js
module.exports = {
  plugins: [
    // Global plugins
  ],
  overrides: [
    {
      test: ['./src/modern/**/*.{js,jsx,ts,tsx}', './src/features/**/*.{js,jsx,ts,tsx}'],
      plugins: [
        'babel-plugin-react-compiler'
      ]
    },
    {
      test: './src/legacy/**/*.{js,jsx,ts,tsx}',
      plugins: [
        // Different plugins for legacy code
      ]
    }
  ]
};
```
You can also configure compiler options per override:

```
// babel.config.js
module.exports = {
  plugins: [],
  overrides: [
    {
      test: './src/experimental/**/*.{js,jsx,ts,tsx}',
      plugins: [
        ['babel-plugin-react-compiler', {
          // options ...
        }]
      ]
    },
    {
      test: './src/production/**/*.{js,jsx,ts,tsx}',
      plugins: [
        ['babel-plugin-react-compiler', {
          // options ...
        }]
      ]
    }
  ]
};
```
For maximum control, you can use `compilationMode: 'annotation'` to only compile components and hooks that explicitly opt in with the `"use memo"` directive.

```
// babel.config.js
module.exports = {
  plugins: [
    ['babel-plugin-react-compiler', {
      compilationMode: 'annotation',
    }],
  ],
};
```
Add `"use memo"` at the beginning of functions you want to compile:

```
function TodoList({ todos }) {
  "use memo"; // Opt this component into compilation
  const sortedTodos = todos.slice().sort();
  return (
    <ul>
      {sortedTodos.map(todo => (
        <TodoItem key={todo.id} todo={todo} />
      ))}
    </ul>
  );
}
function useSortedData(data) {
  "use memo"; // Opt this hook into compilation
  return data.slice().sort();
}
```
With `compilationMode: 'annotation'`, you must:

- Add `"use memo"` to every component you want optimized
- Add `"use memo"` to every custom hook
- Remember to add it to new components

This gives you precise control over which components are compiled while you evaluate the compiler’s impact.

The `gating` option enables you to control compilation at runtime using feature flags. This is useful for running A/B tests or gradually rolling out the compiler based on user segments.

The compiler wraps optimized code in a runtime check. If the gate returns `true`, the optimized version runs. Otherwise, the original code runs.

```
// babel.config.js
module.exports = {
  plugins: [
    ['babel-plugin-react-compiler', {
      gating: {
        source: 'ReactCompilerFeatureFlags',
        importSpecifierName: 'isCompilerEnabled',
      },
    }],
  ],
};
```
Create a module that exports your gating function:

```
// ReactCompilerFeatureFlags.js
export function isCompilerEnabled() {
  // Use your feature flag system
  return getFeatureFlag('react-compiler-enabled');
}
```
If you encounter issues during adoption:

1. Use `"use no memo"` to temporarily exclude problematic components
2. Check the [debugging guide](https://react.dev/learn/react-compiler/debugging) for common issues
3. Fix Rules of React violations identified by the ESLint plugin
4. Consider using `compilationMode: 'annotation'` for more gradual adoption

- Read the [configuration guide](https://react.dev/reference/react-compiler/configuration) for more options
- Learn about [debugging techniques](https://react.dev/learn/react-compiler/debugging)
- Check the [API reference](https://react.dev/reference/react-compiler/configuration) for all compiler options
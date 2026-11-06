---
id: "llms_058"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 58
source_url: "https://huggingface.co/docs/reachy_mini"
language: "en"
retrieved_at: "2026-11-01 22:41:23"
content_hash: "f7caa29f6151d9d4d9bc270d7f1461d38321d8478749f7cbb696d3da8a216a75"
---

# LLMs

Source: https://huggingface.co/docs/reachy_mini

---

Reachy Mini documentation

Reachy Mini 🤖

# 

**Reachy Mini is an open-source, expressive robot made for hackers and AI builders.**

## 

**Choose your platform to access the specific guide:**

| **🤖 Reachy Mini (Wireless)** | **🔌 Reachy Mini Lite** | **💻 Simulation** | 
|---|---|---|
| The full autonomous experience. Raspberry Pi CM4 + Battery + WiFi. | The developer version. USB connection to your computer. | No hardware required. Prototype in MuJoCo. | 
| 👉 [**Go to Wireless Guide**](https://huggingface.co/platforms/reachy_mini/get_started) | 👉 [**Go to Lite Guide**](https://huggingface.co/platforms/reachy_mini_lite/get_started) | 👉 [**Go to Simulation**](https://huggingface.co/platforms/simulation/get_started) | 

⚡ **Pro tip:** Install [uv](https://docs.astral.sh/uv/getting-started/installation/) for 10-100x faster app installations (auto-detected, falls back to `pip`).


## 

Reachy Mini comes with an app store powered by Hugging Face Spaces. You can install these apps directly from Reachy Mini Control with one click!

- **🗣️ [Conversation App](https://huggingface.co/spaces/pollen-robotics/reachy_mini_conversation_app):** Talk naturally with Reachy Mini (powered by LLMs).
- **📻 [Radio](https://huggingface.co/spaces/pollen-robotics/reachy_mini_radio):** Listen to the radio with Reachy Mini !
- **👋 [Hand Tracker](https://huggingface.co/spaces/pollen-robotics/hand_tracker_v2):** The robot follows your hand movements in real-time.

👉 **Browse all apps on Hugging Face**

## 

### 

Most Reachy Mini apps are **web / JS apps**: a static page that drives the robot over WebRTC from any browser, with zero install for whoever uses it. This is the recommended path for new apps. The fastest way is to describe your idea to an AI coding agent:

*I’d like to build a Reachy Mini web app that **\[waves when I say hello\]**. Read [https://github.com/pollen-robotics/reachy\_mini/blob/main/AGENTS.md](https://github.com/pollen-robotics/reachy_mini/blob/main/AGENTS.md) first — it has everything you need.*


Prefer to stay in Python for on-robot control loops? The Python SDK is still available:

```
from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
with ReachyMini() as mini:
    # Look up and tilt head
    mini.goto_target(
        head=create_head_pose(z=10, roll=15, degrees=True, mm=True),
        duration=1.0
    )
```
### 

- **[Installation](https://huggingface.co/SDK/installation)**: 5 minutes to set up your computer
- **[Quickstart Guide](https://huggingface.co/SDK/quickstart)**: Run your first behavior on Reachy Mini
- **[JavaScript SDK & Web Apps](https://huggingface.co/SDK/javascript-sdk)**: Build browser apps that drive the robot over WebRTC — **the easiest way to share your apps**.
- **[Building & Publishing Apps](https://huggingface.co/SDK/apps)**: Create, test, publish, and debug Reachy Mini apps.
- **[AI Integrations](https://huggingface.co/SDK/integration)**: Connect LLMs, build Apps, and publish to Hugging Face.
- **[Core Concepts](https://huggingface.co/SDK/core-concept)**: Architecture, coordinate systems, and safety limits.
- **[Python SDK](https://huggingface.co/SDK/python-sdk)**: Full robot control from Python — scripts, control loops, and on-robot code.
- **[Tutorials](https://huggingface.co/sdk-tutorials)**: Hands-on Jupyter notebooks to learn the SDK step by step.
- 📂 [**Browse the Examples Folder**](https://github.com/pollen-robotics/reachy_mini/tree/main/examples)

## 

Reachy Mini robots are sold as kits and generally take **2 to 3 hours** to assemble. Detailed step-by-step guides are available in the platform-specific folders linked above.

- **Reachy Mini (Wireless):** Runs onboard (RPi CM4), autonomous, includes IMU. [See specs](https://huggingface.co/platforms/reachy_mini/hardware).
- **Reachy Mini Lite:** Runs on your PC, powered via wall outlet. [See specs](https://huggingface.co/platforms/reachy_mini_lite/hardware).

## 

Encountering an issue? 👉 [Check the Troubleshooting & FAQ Guide](https://huggingface.co/troubleshooting)

## 

- **Join the Community:** Join [Discord](https://discord.gg/2bAhWfXme9) to share your moments with Reachy, build apps together, and get help.
- **Found a bug?** Open an issue on [this repository](https://github.com/pollen-robotics/reachy_mini/issues).
- **Next Steps:** Check out our [roadmap](https://huggingface.co/troubleshooting/roadmap) and share your feedback!

## 

This project is licensed under the Apache 2.0 License. See the [LICENSE](https://github.com/pollen-robotics/reachy_mini/tree/main/LICENSE) file for details.
Hardware design files are licensed under Creative Commons BY-SA-NC.

[Update on GitHub](https://github.com/pollen-robotics/reachy_mini/blob/main/docs/source/index.mdx)
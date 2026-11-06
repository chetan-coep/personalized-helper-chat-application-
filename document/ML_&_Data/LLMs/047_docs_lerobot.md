---
id: "llms_047"
technology: "LLMs"
category: "ML & Data"
title: "LLMs"
doc_order: 47
source_url: "https://huggingface.co/docs/lerobot"
language: "en"
retrieved_at: "2026-11-01 22:41:01"
content_hash: "87807dc22ff82e7d21a5815fef83da39f2d6dd193f190484c3ab644ccbff0cc7"
---

# LLMs

Source: https://huggingface.co/docs/lerobot

---

LeRobot documentation

LeRobot

# 

**State-of-the-art machine learning for real-world robotics**

🤗 LeRobot provides a hardware-agnostic, Python-native interface for controlling real robots - from affordable arms like the SO-ARM101 to full humanoids. Plus the tools to record, store, and share the datasets they generate. Every dataset uses the standardized **LeRobotDataset** format (synchronized video + action/state data) and can be streamed directly from the [Hugging Face Hub](https://huggingface.co/lerobot).

🤗 On top of that data, LeRobot implements state-of-the-art policies - from lightweight imitation-learning models like ACT to large vision-language-action models like π₀ and SmolVLA - all trainable, shareable, and deployable with the same handful of CLI commands.

The goal: lower the barrier to entry for robotics, so that everyone can contribute to, and benefit from, shared datasets and pretrained models.

## 

**Teleoperate → Record → Train → Deploy**

1. **Teleoperate** - control the robot yourself (with a leader arm, keyboard, or phone) so it can learn from your movements.
2. **Record** - each demonstration is saved as a dataset: synchronized camera video plus the actions you took.
3. **Train** - a policy (the neural network that will control the robot) learns to imitate your demonstrations.
4. **Deploy** - run the trained policy on the robot and watch it complete the task on its own.

## 

New here? [Install LeRobot](https://huggingface.co/installation), then pick your path:

LeRobot supports a wide range of arms and mobile robots. Popular picks:

- [SO-101](https://huggingface.co/so101) - our flagship, low-cost arm
- [LeKiwi](https://huggingface.co/lekiwi) - a mobile base with an arm on top
- [Koch v1.1](https://huggingface.co/koch) - a long-time community favorite
- or find yours under **Robots** in the sidebar

Once it's assembled and calibrated, record a dataset and train your first
      policy with the [imitation learning tutorial](https://huggingface.co/il_robots) - or
      skip the CLI entirely with [LeLab](https://huggingface.co/lelab), a browser GUI for
      the same workflow.

You can still train and evaluate policies without owning a robot:

- train on an existing [LeRobot dataset](https://huggingface.co/datasets?other=LeRobot) from the Hub
- evaluate in [simulation](https://huggingface.co/envhub), against benchmarks like
        LIBERO or Meta-World
- try the free [Colab notebooks](https://huggingface.co/notebooks) - nothing to
        install

Start with the [Contributing guide](https://huggingface.co/contributing), then [add a new policy](https://huggingface.co/bring_your_own_policies) or [bring your own hardware](https://huggingface.co/integrate_hardware).

## 

## 

Running into issues? A few of the most frequent ones:

- **Blurry or unusable camera footage** - lighting matters more than resolution. See the [Cameras](https://huggingface.co/cameras) guide.
- **Build or install errors** (`cmake`, `ffmpeg`, CUDA) - see the Troubleshooting section of the [Installation guide](https://huggingface.co/installation#troubleshooting).
- **Not sure which policy fits your GPU** - check the [Compute & Hardware Guide](https://huggingface.co/hardware_guide).
- **Still stuck?** Ask on [Discord](https://discord.gg/s3KuuzsPFb) - the community (and the LeRobot team) is there to help.

[Update on GitHub](https://github.com/huggingface/lerobot/blob/main/docs/source/index.mdx)
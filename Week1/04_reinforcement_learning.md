# Reinforcement Learning

## Definition

An agent learns to make decisions by interacting with an environment. It takes actions, receives rewards or penalties, and adjusts its behavior (policy) to maximize cumulative reward over time.

## Key components

- **Agent** — the learner/decision maker
- **Environment** — everything the agent interacts with
- **State** — current situation of the agent
- **Action** — what the agent can do
- **Reward** — feedback signal for an action
- **Policy** — the strategy the agent uses to pick actions

## How it's different from supervised learning

There's no fixed dataset of "correct" actions — the agent has to explore and discover what works through trial and error, balancing:
- **Exploration** — trying new actions to discover their effects
- **Exploitation** — using known good actions to maximize reward

## My own example

Training an agent to play a simple game like Snake — it doesn't know beforehand which moves are good, but learns over many episodes that moving toward food and avoiding walls leads to higher rewards.

## Questions to revisit

- How is the exploration-exploitation tradeoff actually tuned in practice?
- What makes reward design so tricky (reward hacking)?
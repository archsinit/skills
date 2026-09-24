# Prosen

Prosen is a small writing skill for agent-produced prose.

Its rule is simple:

> Write for the reader, not for the appearance of good writing.

It does not try to make text statistically "human." It does not ban ordinary words, force sentence-length variation, or add quirks for authenticity. It asks the agent to say what it means, trust the reader, keep necessary reasoning, and stop when the prose works.

The whole skill lives in [SKILL.md](SKILL.md).

## Early comparison

This is not a benchmark or ranking. It is one prompt written four ways so the differences are visible.

The three external examples below use the published guidance from:

- [Humanizer](https://github.com/spuvr/humanizer)
- [Slopless](https://github.com/BioInfo/slopless)
- [Human Writing](https://github.com/1999AZZAR/human-writing-skill)

All four versions use the same prompt.

### Prompt

> Write a short essay about how tools that are supposed to make work easier can sometimes make the work harder. Use ordinary workplace examples. Keep it under 300 words.

### Humanizer

At 9:07 on Monday morning, someone is copying a customer name from Slack into Jira, then opening the CRM to paste it there too. None of these tools is broken. In fact, each one probably solved a real problem when the company bought it.

The trouble starts when every solution asks the worker to become the glue.

A new project tracker makes assignments clearer, but now someone has to keep the tracker current. A meeting recorder saves notes, but people still have to review the transcript, pull out the decisions, and move them somewhere useful. The expense app replaces paper receipts with photographs, categories, approval rules, and the occasional fifteen-minute argument with a dropdown menu.

This is how work gets heavier without looking heavier. The old task disappears, but a layer of coordination takes its place.

Sometimes the extra layer is worth it. A shared system can make work visible to people who were previously guessing. But a tool should remove more effort than it creates. That sounds obvious until a company has twenty of them, each saving time inside its own little box.

The person doing the job experiences the boxes all at once.

### Slopless

A tool can remove one task and create three smaller ones around it.

Take project management software. Before it arrives, a team may coordinate badly through email and meetings. After it arrives, assignments are easier to see, but someone has to update statuses, maintain fields, clean up stale tickets, and remind everyone to use the system correctly.

The same thing happens with communication tools. Slack makes a quick question easier than writing an email. It also creates another place to check, another stream of interruptions, and another archive where a decision can disappear.

Automation can do this too. A form may save ten minutes of manual entry while adding approval rules, exception handling, and troubleshooting that nobody counted when the tool was chosen.

None of this makes the tools useless. The mistake is measuring only the work they remove.

A useful tool reduces the total effort required to get the job done. That includes the time spent feeding it, checking it, fixing it, and moving information between it and everything else.

If people spend more time managing the system than benefiting from it, the system has become part of the workload.

### Human Writing

Workplace tools make work harder when the coordination and maintenance they introduce outweigh the task they were meant to simplify.

A project management system, for example, can make ownership and deadlines easier to see. It also requires people to update tasks, maintain fields, close outdated items, and learn a shared workflow. If the team still coordinates through email and meetings, the new system may add another layer rather than replace one.

Communication tools create a similar tradeoff. Instant messaging makes quick questions convenient, but it can fragment decisions across channels and increase interruptions. Employees may spend less time composing formal messages while spending more time monitoring conversations and searching for information later.

Automation has its own maintenance cost. A workflow that saves routine data entry may still require exception handling, approvals, monitoring, and troubleshooting.

The relevant question is therefore not whether a tool makes one task faster. It is whether the tool reduces the total effort required to complete the work.

That total includes learning the system, keeping it accurate, handling failures, and connecting it to the rest of the workplace. A tool is useful when those costs remain lower than the work it removes.

### Prosen

A new tool rarely arrives alone. It brings a login, a workflow, a set of fields to keep current, and one more place where information can live.

A project tracker can make deadlines easier to see. It can also leave the team updating tickets after the real conversation already happened in a meeting. Slack makes quick questions painless, but now a decision might be in email, Slack, the project tracker, or someone's notes. An automated approval can save routine work until an unusual case appears and nobody knows why the request is stuck.

The problem is not that these tools are bad. Most of them solve something.

The problem is that companies tend to count the work a tool removes and ignore the work needed to support the tool itself. Someone has to enter the information, keep it accurate, handle exceptions, and connect it to everything around it.

Sometimes that extra work is a good trade. Shared systems can prevent missed handoffs and make a growing team easier to coordinate.

But the test should be the whole job, not the feature the tool replaced. If a five-minute task disappears and ten minutes of maintenance takes its place, the work did not get easier. It moved.

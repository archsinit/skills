# Prosen

Prosen is a writing skill for AI agents. It helps them draft and revise prose that says what it means, keeps the reasoning intact, and trusts the reader.

The user and the genre decide what to say. Prosen guides how to say it: lead with the substance, find the central idea in longer work, use concrete language when the facts support it, and let the material determine the structure. A memo, a story, and a poem should have room to sound different.

When rewriting, preserve claims, uncertainty, commitments, and necessary nuance. Cut repetition and rhetorical padding without cutting the reasoning. If the prose already works, leave it alone.

## Use Prosen

In an agent that supports writing skills, load [SKILL.md](SKILL.md) and ask for the prose you need. For example:

```text
Use Prosen to rewrite this memo. Preserve the facts, commitments,
and uncertainty. Return only the revised memo.
```

Prosen applies to documents, essays, reports, READMEs, emails, posts, instructions, descriptions, and other reader-facing prose. It does not apply to ordinary chat unless you ask. The complete skill is one file; there are no supporting scripts or reference files to load.

## Four skills, nine prompts

This comparison uses the same nine prompts with **Humanizer**, **Slopless**, **Human Writing**, and **Prosen**. It includes 36 responses: one per skill per prompt. The complete prompts and outputs appear below.

Some responses were very close. In the Invoice Watcher README test, Human Writing and Prosen produced the same two body paragraphs apart from “It is” versus “It’s”; Human Writing included a heading, while Prosen did not. The expense emails also followed much the same wording and sequence. A writing skill does not necessarily produce a visibly different answer to a tightly specified request.

Other prompts exposed different choices. Humanizer opened the payroll explainer with an employee calling in sick two days before payday. The other three began by stating the dependency risk. For backup instructions, Human Writing used numbered steps; the others kept the procedure in a paragraph. These are differences a reader can inspect, rather than scores assigned to a skill.

| Test | What differs in these responses |
|---|---|
| Technical documentation | Human Writing breaks restoration into three numbered steps. Prosen keeps the steps inline and bolds the interface labels. Humanizer and Slopless use plain paragraphs. |
| Business memo | All four lead with the pilot recommendation. Slopless ends with an explicit condition that unresolved payroll problems should hold up expansion. Human Writing and Prosen end with a review of the findings before deciding whether to proceed. |
| Explainer | Humanizer starts with a payroll employee calling in sick. Slopless, Human Writing, and Prosen state the risk first. All four discuss documentation and backup coverage. |
| Short essay | Humanizer opens inside a support team's Thursday afternoon. Slopless follows a ticket-count example with deadline incentives. Human Writing also examines meeting participation. Prosen starts with call length, then examines hiring targets and incomplete orders. |
| Workplace email | Humanizer and Human Writing are nearly identical. Slopless omits a sign-off. Prosen keeps the greeting and sign-off but omits the separate reminder to submit by the new deadline. |
| README | Human Writing and Prosen have nearly identical body text but differ on whether to include a heading. Humanizer adds a closing instruction to put an invoice in the folder. Slopless uses one paragraph without a heading. |
| Narrative | All four use small office routines: mugs, belongings, lights, and unfinished work. Humanizer ends with a door needing a second pull. Human Writing and Prosen end with the employee checking the door and heading toward or down the stairs. |
| Poem | Humanizer ends on keys catching in a coat lining. Slopless ends on checking the door. Human Writing ends with “leaves tomorrow on the desks.” Prosen ends on a pencil marking where work will resume. |
| Rewrite | Humanizer, Slopless, and Human Writing retain “important step”; Slopless and Human Writing also retain “valuable resource.” Prosen removes both phrases and opens with what the knowledge base provides. |

The rewrite gives a concrete example of Prosen's treatment of rhetorical framing. The source opens by calling the knowledge base “an important step forward.” Prosen's response opens with its function: giving employees a central place to find information. The [skill](SKILL.md) permits removing judgments that add no factual content while preserving claims and their qualifiers. This response shows that choice; one run does not establish how reliably it will recur.

## Test conditions and limits

The tests ran on **24 September 2026**, using **Codex CLI 0.155.0-alpha.9.2**, **gpt-6-astra**, and **medium reasoning**, on Windows with PowerShell 7.6.5. No temperature, top-p, or seed override was supplied.

**Prosen was updated and rerun on all nine prompts.** This README pairs those fresh responses with the original 27 responses from Humanizer, Slopless, and Human Writing. The exact prompt files, model, CLI binary, reasoning setting, and execution configuration were held constant. The earlier Prosen responses are not used in this comparison.

Each response came from a fresh ephemeral session with its own working directory and runtime. Only the assigned skill was enabled. Its complete text and required references were preloaded into the project instructions. Previous outputs were never supplied as context, and file-reading tools, web access, plugins, and delegation were disabled. The accepted runs made no tool calls.

These are the exact versions tested:

| Skill | Source | Pinned revision |
|---|---|---|
| Humanizer | [spuvr/humanizer](https://github.com/spuvr/humanizer) | [0d5a8cf82bc36232b79afafd4993ca4f8226c8bd](https://github.com/spuvr/humanizer/commit/0d5a8cf82bc36232b79afafd4993ca4f8226c8bd) |
| Slopless | [BioInfo/slopless — writing voice](https://github.com/BioInfo/slopless/blob/2a32d0c001777c7ddfa3f9a5909a8925df4722cf/rules/writing-voice.md) | [2a32d0c001777c7ddfa3f9a5909a8925df4722cf](https://github.com/BioInfo/slopless/commit/2a32d0c001777c7ddfa3f9a5909a8925df4722cf) |
| Human Writing | [1999AZZAR/human-writing-skill](https://github.com/1999AZZAR/human-writing-skill) | [7c0de1fb37192aed1e72af14c2b2b19dbe060f7e](https://github.com/1999AZZAR/human-writing-skill/commit/7c0de1fb37192aed1e72af14c2b2b19dbe060f7e) |
| Prosen | [archsinit/skills — Prosen](https://github.com/archsinit/skills/blob/343739e4c62648521bd2a67469f565201217b365/skills/prosen/SKILL.md) | [343739e4c62648521bd2a67469f565201217b365](https://github.com/archsinit/skills/commit/343739e4c62648521bd2a67469f565201217b365) |

Slopless was tested through a minimal skill wrapper around its unchanged writing-voice file. Its other rules and hooks were not loaded. The Prosen revision above is the commit that last changed its skill file; that file was still current when the nine new runs began.

The first Humanizer documentation attempt was excluded after Codex reported an unsupported configuration setting. It was rerun in a fresh session after that setting was removed. All 36 responses shown here used the corrected configuration and completed successfully. The nine updated-Prosen runs needed no retries. Every response from that batch is included; none was selected or discarded for its writing quality.

There was only one accepted response per tested skill version per prompt, one model, and no run without a writing skill. Prosen was revised after the earlier test round and retested on the same prompts, so this is not a held-out evaluation. The other three skills were not updated or rerun, and their pinned versions may differ from their latest releases. The hosted model was not a frozen weight snapshot, and generation was not deterministic. We therefore cannot separate stable skill effects from model behavior and sampling variation. These observations describe this set of outputs, not a ranking of the skills or a survey of every writing skill available.

## Read the complete outputs

Every category below contains all four responses, copied unchanged from the saved final outputs. None has been shortened, corrected, or rewritten for this README. Poems appear in text blocks to preserve their line breaks. The summary above is commentary on those responses.

This exact instruction preceded every category prompt:

> Use only the project writing skill provided for this run. Do not use any other writing or style skill. Return only the requested prose. Do not explain your writing choices.

The category prompts below preserve their submitted wording. Markdown blockquote markers used to display the original request were not part of the submitted text.

<details>
<summary>Test 1 — Technical documentation</summary>

### Category prompt

Write a short documentation section explaining how backups work in a desktop application.

Facts you must preserve:
- The application automatically creates a backup every 30 minutes.
- Backups are kept locally for 24 hours.
- To restore one, the user opens Settings > Backups, selects a snapshot, and chooses Restore.
- Restoring closes the application for about one to three minutes.
- Unsaved changes made after the selected snapshot are lost.

Write for an ordinary user, not a developer. Keep it under 180 words.

### Humanizer

The application automatically creates a backup every 30 minutes and keeps each backup on your computer for 24 hours.

To restore a backup, open Settings > Backups, select a snapshot, and choose Restore. The application closes for about one to three minutes while it restores the backup.

Unsaved changes made after the selected snapshot will be lost.

### Slopless

The application automatically creates a backup every 30 minutes and keeps each backup locally on your computer for 24 hours.

To restore a backup, open Settings > Backups, select a snapshot, and choose Restore. The application closes for about one to three minutes while it restores the backup. Any unsaved changes made after the selected snapshot are lost.

### Human Writing

The application automatically creates a backup every 30 minutes and keeps each backup on your device for 24 hours.

To restore a backup:

1. Open **Settings > Backups**.
2. Select a snapshot.
3. Choose **Restore**.

Restoring closes the application for about one to three minutes. Unsaved changes made after the selected snapshot are lost.

### Prosen

The application automatically creates a backup every 30 minutes and keeps each backup on your computer for 24 hours.

To restore a backup, open **Settings > Backups**, select a snapshot, and choose **Restore**.

Restoring closes the application for about one to three minutes. Unsaved changes made after the selected snapshot are lost.

</details>

<details>
<summary>Test 2 — Business memo</summary>

### Category prompt

Write a short internal memo recommending that a company pilot a new timekeeping system with one department before rolling it out company-wide.

Facts:
- The company has 420 employees.
- The proposed pilot department has 58 employees.
- The pilot would last six weeks.
- The current system will remain available during the pilot.
- The main purpose is to find workflow and payroll problems before a company-wide rollout.
- A pilot may delay the full rollout by about one month.

Make a clear recommendation and explain the main tradeoff. Keep it under 220 words.

### Humanizer

I recommend a six-week pilot of the new timekeeping system in the proposed department of 58 employees before we roll it out to all 420 employees.

The pilot would let us see how the system handles everyday time entry, approvals, and payroll, and catch problems while they affect a smaller group. The current system would remain available throughout the pilot so the department has a fallback if problems arise.

The tradeoff is timing: a pilot may push the full rollout back by about one month. That delay is worth taking to find workflow and payroll problems before the whole company depends on the new system. Fixing those problems across 58 employees would be more manageable than doing so across 420.

We should use the six weeks to document issues, test fixes, and decide whether the system is ready for a company-wide rollout.

### Slopless

I recommend a six-week pilot of the new timekeeping system in the proposed 58-employee department before we roll it out to all 420 employees. Keep the current system available throughout the pilot.

The purpose is to find workflow and payroll problems while the rollout is limited to one department, so we can address them before expanding. Payroll errors would affect fewer people. The pilot should help us identify where employees struggle to record time and where payroll processing needs correction.

The tradeoff is timing. A pilot may delay the full rollout by about one month, but it gives us a chance to catch problems before all 420 employees depend on the new system. That delay is worth accepting.

At the end of six weeks, review the workflow and payroll findings and use them to decide whether to proceed with the company-wide rollout. Unresolved payroll problems should hold up expansion.

### Human Writing

I recommend a six-week pilot of the new timekeeping system with the proposed 58-person department before rolling it out to all 420 employees. The pilot would help us identify workflow and payroll problems while they affect a smaller group. The current system would remain available throughout the pilot.

The main tradeoff is timing: a pilot may delay the company-wide rollout by about one month. That delay is worthwhile because it gives us a chance to address problems before they affect the entire company.

At the end of the six weeks, we should review the problems found and any unresolved issues before deciding whether to proceed with the full rollout.

### Prosen

I recommend piloting the new timekeeping system with the proposed 58-employee department for six weeks before rolling it out to all 420 employees. The pilot’s main purpose would be to identify workflow and payroll problems while they affect a smaller group. The current system would remain available throughout the pilot.

The tradeoff is timing: a pilot may delay the full rollout by about one month. That delay would give us time to find and address problems that could otherwise disrupt timekeeping or payroll across the company.

At the end of the six weeks, we should review the findings and decide whether the system is ready for company-wide use or needs further work.

</details>

<details>
<summary>Test 3 — Explainer</summary>

### Category prompt

Explain to a small-business owner why relying on one employee to know the entire payroll process creates operational risk.

Do not sell a product or service. Do not assume that outsourcing is the solution.

Keep it under 180 words.

### Humanizer

Your payroll person calls in sick two days before payday. Someone else can log in, but they don't know which timesheets need correcting, how overtime is checked, or when the bank needs the payment file.

That's the risk of having the whole process in one employee's head. A routine absence can delay wages or lead to mistakes that take days to untangle. If that employee leaves suddenly, you may be rebuilding the process while staff are waiting to be paid.

It also makes errors harder to catch. When only one person understands the calculations and adjustments, everyone else has to accept the results without much ability to check them. Even a careful, trusted employee needs a second pair of eyes.

Keep a written payroll schedule and clear instructions, with secure access arranged for an authorized backup. Have that person run payroll under supervision occasionally. The useful test is whether someone else can get people paid correctly and on time when your usual payroll person is unavailable.

### Slopless

When one employee knows the entire payroll process, their availability determines whether everyone else gets paid correctly and on time. An unexpected absence can expose the gap. Someone covering for them may have access to the payroll system but still not know how to handle overtime, deductions, corrections, or filing deadlines.

Mistakes also become harder to catch. If the same person prepares payroll and checks their own work, an incorrect pay rate or missed adjustment can carry into later pay periods. Employees then have to flag errors themselves.

The employee may be excellent at their job. The risk comes from leaving the business dependent on knowledge that nobody else can use when that person is unavailable or leaves.

Start with the next payroll run. Have the employee document each step, including deadlines and exceptions, then let a backup work through those instructions while the employee checks the result. Keep access secure and arrange a second review before payment. That practice run will reveal gaps while someone can still explain them.

### Human Writing

When only one employee knows how payroll works, your ability to pay people correctly and on time depends on that person being available. An illness, unexpected departure, or even a holiday can leave you scrambling to work out deadlines, deductions, approvals, and corrections.

The risk goes beyond absence. If nobody else understands the process, mistakes can be harder to spot. A missed adjustment or filing deadline may go unnoticed until an employee raises a concern or a penalty arrives. The person handling payroll also has little backup when an unusual problem comes up.

Reduce that dependence by documenting each payroll step, keeping deadlines and access instructions somewhere secure, and training a second person to run the process. Have that person complete a payroll cycle while the usual employee checks their work. Keep a separate review of pay totals and changes before approval.

This gives your business a workable backup and lets the employee take time off without remaining on call for payroll.

### Prosen

If only one employee knows how to run payroll, their absence can put payday at risk. A sudden illness, resignation, or family emergency may leave you with the payroll software but no one who knows how to complete the work.

The missing knowledge is often in the details: when hours must be approved, how overtime and deductions are handled, which exceptions need checking, and when payments and tax filings are due. Reconstructing those steps under a deadline increases the chance of late pay, incorrect amounts, or missed obligations. Errors can take time to fix and undermine employees’ trust.

Even while that person is available, mistakes can go unnoticed if no one else understands the process well enough to review it.

Reduce the dependency by documenting the steps and deadlines, arranging secure backup access, and training a second person. Have the backup run payroll with supervision so you know the business can manage an absence.

</details>

<details>
<summary>Test 4 — Short essay</summary>

### Category prompt

Write a short essay about how measuring work can sometimes change the work itself.

Use ordinary workplace examples. Do not cite research or invent statistics.

Keep it under 300 words.

### Humanizer

By Thursday afternoon, the support team has learned to leave the awkward tickets alone. A password reset takes minutes. A billing problem might take six emails and a conversation with someone in accounts. If Friday's report ranks people by tickets closed, the sensible move is to clear the easy ones first.

Nobody has to tell the team to do this. The report does enough.

Measuring work gives people a clue about what will count when their manager asks how things are going. That clue can be useful. A growing backlog deserves attention, and a deadline can pull a drifting project back into focus. But people also start arranging their days around whatever appears on the chart. The billing problem can wait, even though the customer has already waited a week.

Something similar happens when an office starts tracking how quickly employees reply to messages. People keep the chat window open. Replies get faster, while the budget that requires an uninterrupted hour gets pushed into the evening. On the report, everyone looks more responsive. They are also answering messages about why the budget is late.

The difficulty is that the numbers may be accurate. The team really did close more tickets. Replies really did arrive sooner. A manager can praise the improvement without seeing what it cost.

Before celebrating a better number, it helps to ask what people had to put off to achieve it. Someone will probably have an example. They may have been meaning to bring it up.

### Slopless

A support team starts counting how many tickets each person closes. The appeal is obvious. A manager can see who has a crowded queue and where customers are waiting, without reading every exchange. But once that count becomes a target, it can change which tickets people want to answer.

A password reset is quick. A recurring billing error might take an afternoon of checking records and talking to another department, yet each counts as one closed ticket. Someone who stays with the billing problem can look less productive than someone who clears a batch of simple requests. The count makes patience expensive.

The same thing can happen with deadlines. If a team gets credit for launching a feature by Friday, people may move unfinished details into follow-up tasks so the launch still qualifies as done. Friday’s report looks tidy. Monday’s work is messier.

This does not make measurement useless. Counting unfinished requests can expose a backlog that everyone has grown used to, and tracking missed deadlines can help a team stop promising more than it can deliver. The trouble starts when the number becomes the easiest way to win approval. People learn its rules.

A manager reviewing closed tickets can also ask which problems keep coming back and which difficult cases someone carried through to a lasting fix. That takes more attention. It may mean reading the exchange behind a low ticket count before asking that employee to work faster.

### Human Writing

A measure can start as a way to understand work and become a reason to do it differently. Once people know which number will appear in a review, they have a practical reason to pay attention to it.

Consider a help desk that tracks how many tickets each employee closes. The count gives managers a rough sense of activity. But if closing tickets becomes the main sign of good performance, an employee may favor simple requests over a difficult problem that takes most of an afternoon. A colleague who fixes the underlying cause of repeated complaints may close fewer tickets while saving everyone time.

The same tension can appear in meetings. A manager who wants more participation might count how often each person speaks. Quiet employees could gain a useful prompt to contribute. Others might learn to speak before they have anything to add. The count captures both, even though their value to the conversation differs.

This does not make measurement pointless. A shared target can clarify expectations or reveal neglected work. Tracking unanswered customer messages, for example, can help a team notice requests that would otherwise be forgotten. The trouble begins when the number becomes a complete account of what matters.

A useful review leaves room to discuss what sits behind the measure. Why did one request take so long? Did the customer need to contact the team again? What work prevented a problem that never became a ticket? Those questions take more effort than comparing totals, but they help keep the measure connected to the job it was meant to improve.

### Prosen

A support worker can end a call quickly by giving a customer a link. Staying on the line while the customer tries the instructions takes longer. If the team is judged by average call length, the quicker call looks better, even when the customer has to call back.

The measure becomes part of the job. Workers learn which choices improve their numbers, and those choices can gradually change what they consider a good day’s work. A problem solved used to be enough. Now it may feel like a poor result if solving it took too long.

This happens even when nobody is trying to cheat. A manager asks a hiring team to fill vacancies faster because departments are short of staff. The team gives priority to roles with plenty of applicants. A difficult vacancy stays open longer because working on it produces little visible progress. Everyone is busy, and the reported results improve, while the department with the hardest role to fill keeps waiting.

Measurement can also reveal work that has been overlooked. Recording how much time employees spend correcting incomplete orders gives a manager a reason to fix the order form. Here, counting the work helps remove some of it.

The difficulty is that a number usually captures only part of what people are trying to accomplish. Once it affects praise, pay, or the next team meeting, that part gets extra attention. A manager reviewing shorter calls needs to leave room for someone to say, “The customer called us three times.”

</details>

<details>
<summary>Test 5 — Workplace email</summary>

### Category prompt

Write an email from an operations manager to all employees announcing a change to the monthly expense reimbursement deadline.

Facts:
- Expense reports were previously due on the 10th of each month.
- They will now be due on the 7th.
- The change begins November 2026.
- Finance needs the extra three days to close the monthly books.
- Reports submitted after the deadline will normally move to the following reimbursement cycle.
- Questions should go to the Finance team.

The tone should be matter-of-fact and respectful. Keep the body under 140 words.

### Humanizer

Subject: Expense reports due on the 7th starting November 2026

Hi everyone,

Starting in November 2026, monthly expense reports will be due on the 7th instead of the 10th. This gives Finance the extra three days it needs to close the monthly books.

Please submit your reports by the new deadline. Reports submitted after the 7th will normally move to the following reimbursement cycle.

If you have questions, please contact the Finance team.

Thank you,
Operations Manager

### Slopless

Subject: Expense report deadline moves to the 7th

Hi all,

Starting in November 2026, please submit monthly expense reports by the 7th of each month so Finance has three extra days to close the monthly books. The previous deadline was the 10th.

Reports submitted after the deadline will normally move to the following reimbursement cycle. Please contact the Finance team with questions.

### Human Writing

Subject: Expense report deadline changes to the 7th starting November 2026

Hi everyone,

Starting in November 2026, monthly expense reports will be due on the 7th instead of the 10th. This gives Finance the extra three days needed to close the monthly books.

Please submit your reports by the new deadline. Reports submitted after the 7th will normally move to the following reimbursement cycle.

If you have questions, please contact the Finance team.

Thank you,
Operations Manager

### Prosen

Subject: Expense report deadline moves to the 7th in November

Hi everyone,

Starting in November 2026, monthly expense reports will be due on the 7th instead of the 10th. This gives Finance three additional days to close the monthly books.

Reports submitted after the deadline will normally move to the following reimbursement cycle.

Please send any questions to the Finance team.

Thank you,
Operations Manager

</details>

<details>
<summary>Test 6 — README / product description</summary>

### Category prompt

Write the opening section of a README for a tool called Invoice Watcher.

The tool watches a folder for newly added PDF invoices, extracts the vendor, invoice number, date, and total, and appends those details to a spreadsheet.

It is intended for small teams that receive invoices as PDFs and currently copy those details into spreadsheets by hand.

Do not invent features.

Keep it under 180 words.

### Humanizer

# Invoice Watcher

Invoice Watcher watches a folder for newly added PDF invoices, extracts the vendor, invoice number, date, and total, and appends those details to a spreadsheet.

It's for small teams that receive invoices as PDFs and copy the details into a spreadsheet by hand. Add an invoice to the folder, and Invoice Watcher takes care of the copying.

### Slopless

Invoice Watcher watches a folder for newly added PDF invoices, extracts the vendor, invoice number, date, and total, and appends those details to a spreadsheet. No copying those fields by hand. It’s built for small teams that receive PDF invoices and track them in spreadsheets.

### Human Writing

# Invoice Watcher

Invoice Watcher watches a folder for newly added PDF invoices, extracts the vendor, invoice number, date, and total, and appends those details to a spreadsheet.

It is built for small teams that receive invoices as PDFs and currently copy those details into spreadsheets by hand.

### Prosen

Invoice Watcher watches a folder for newly added PDF invoices, extracts the vendor, invoice number, date, and total, and appends those details to a spreadsheet.

It’s built for small teams that receive invoices as PDFs and currently copy those details into spreadsheets by hand.

</details>

<details>
<summary>Test 7 — Narrative prose</summary>

### Category prompt

Write a short scene about the last employee leaving a small office at night.

The computers are still running. The employee switches off the lights one section at a time. There is unfinished work waiting for tomorrow.

Nothing dramatic happens.

Keep it under 250 words.

### Humanizer

At the back of the office, a computer fan rattled. Nina rested her hand on the case until it stopped, then put on her coat.

She had got as far as the second invoice. The third was open on her screen, with a number she needed to check against a delivery note. She left the note across her keyboard so she'd see it in the morning.

The switch by the printer turned off the lights over the empty desks. In the dark, the computers looked brighter. Someone had left a spreadsheet open at two hundred percent, one enormous yellow cell filling half the screen.

Nina took her mug to the kitchenette. There was still tea in it. She tipped it out, gave the mug a rinse and left it in the sink.

She switched off the kitchenette, then the strip above her own desk. At the door she felt through both coat pockets for her keys before finding them in her hand, caught under the strap of her bag.

The last switch was beside the alarm panel. She pressed it, stepped into the corridor and pulled the door shut. It needed a second pull to catch.

### Slopless

The last employee rinsed a mug in the small office kitchen and left it upside down beside the sink, where it rocked on a spoon. She moved the spoon. Then she went back for her bag.

Her computer was still running. A spreadsheet filled one screen, and on the other an unfinished email ended halfway through a sentence she would have to read again tomorrow. She saved both and pushed her chair in. Across the aisle, another computer showed a box asking someone to install an update.

She switched off the kitchen lights first. The light over her desk still reached the counter, enough for her to see that she had left the lid of her lunch container there. She fetched it and tucked it into her bag.

At the switches by the door, she turned off the back row, then the row above the desks. The monitors stayed bright. In their light she checked the floor near her chair for anything she had dropped, though she could have done that before.

Her bag caught against the doorframe as she stepped out, and she shifted it onto her other shoulder to get the door shut. She checked the handle and left.

### Human Writing

At a quarter past nine, Nina put a yellow note on the invoice she had been checking. She wrote “check delivery date,” then laid her pen across it.

The computers were still running. Hers had a spreadsheet open; the one beside it showed a photograph of a beach. A fan hummed beneath the empty desk by the window.

She took her mug to the kitchenette, rinsed it, and left it upside down on the draining board. There was half a carton of milk in the fridge. Enough for the morning.

The first switch darkened the kitchenette and the table where they ate lunch. At the next switch, she paused to look back at her desk. Her glasses were beside the keyboard. She fetched them, tucked them into her bag, and turned off the lights over the desks.

In the remaining light by the door, she buttoned her coat. Tomorrow she would have to finish the invoices before answering the messages she had left unread.

She switched off the entrance light, stepped into the corridor, and pulled the door shut. After checking the handle, she walked toward the stairs.

### Prosen

At a quarter past eight, Nina put a note on the invoice she had checked twice: Ask Martin about delivery charge. She left it on top of the others, where she would see it in the morning.

The computers were still running. Hers showed a small box saying the update was six percent complete. She pushed her chair in, then pulled it out again to get her cardigan off the back.

There were three light switches by the door. She turned off the one for the desks. The screens made pale rectangles along the wall, and she could still see her mug beside the keyboard. She went back for it.

In the kitchenette she rinsed the mug and set it upside down on the rack. The sponge had fallen into the sink. She squeezed it out and put it on the edge.

The kitchenette lights went next, then the lights over reception. For a moment she stood with her hand in her bag, feeling past her purse and a folded shopping bag for her keys.

Outside, she tried the office door once to check the lock. She put the keys in her coat pocket and walked down the stairs.

</details>

<details>
<summary>Test 8 — Poem</summary>

### Category prompt

Write a short poem about the last employee leaving a small office at night.

The computers are still running, the lights are being switched off, and unfinished work is waiting for tomorrow.

Keep it under 20 lines.

Do not explain the poem afterward.

### Humanizer

```text
She saves the sheet as it is,
one column short,
and leaves a note across the keys.

Under the desks, the computers hum.
She switches off the light above the printer,
then the one beside the door.

Her coat sleeve brushes a paper cup.
She catches it before it tips,
stands it on tomorrow's invoices.

In the dark she finds her keys
by the little tooth
that always catches in the lining.
```

### Slopless

```text
She pushes her chair beneath the desk.
The computers keep running,
warm air brushing her knees
as she reaches for her bag.

One switch, then another.
The small office darkens
except beneath the desks,
where the power lights stay green.

Tomorrow she will finish the sentence
at the top of the open file.
For now, she checks the door
with a short pull on the handle.
```

### Human Writing

```text
She rinses her cup and leaves it to dry.
Behind her, the computers hum
under the three small desks.

One switch darkens the room;
the next takes the light from the hall.

A spreadsheet glows beside a folded note:
ask about the missing hours.
She almost sits down again.

Then her keys catch in the coat lining.
She works them loose,
locks the door,
and leaves tomorrow on the desks.
```

### Prosen

```text
She leaves the figures half checked,
a pencil laid across the doubtful row.

One switch takes the light from the desks,
the other from the sink.
Blue screens show the backs
of four empty chairs.

At the door she listens
to the computers’ small, steady fans,
then pulls until the latch catches.

Tomorrow she will start
where the pencil is.
```

</details>

<details>
<summary>Test 9 — Rewrite</summary>

### Category prompt

Rewrite the passage below.

Preserve every factual claim and do not add new facts. Improve only the prose.

Keep approximately the same amount of information. Do not explain your edits.

Original passage:

The implementation of the new internal knowledge base represents an important step forward in the organization's ongoing efforts to improve information accessibility and enhance cross-functional collaboration. The platform provides employees with a centralized location where they can access policies, procedures, departmental documentation, and other relevant resources. This will not only help reduce the amount of time employees spend searching for information, but also empower teams to work more efficiently and make better-informed decisions. It is important to note that the success of the platform will ultimately depend on departments keeping their content accurate and up to date. As the organization continues to grow and evolve, the knowledge base will serve as a valuable resource that supports employees and helps create a more connected and informed workplace.

### Humanizer

The new internal knowledge base is an important step in making information easier to find and helping departments work together. It gives employees one place to access policies, procedures, departmental documentation, and other relevant resources. With less time spent searching for information, teams will be able to work more efficiently and make better-informed decisions.

The platform's success will depend on departments keeping their content accurate and up to date. As the organization grows and changes, the knowledge base will continue to support employees and help them stay informed and connected across departments.

### Slopless

The new internal knowledge base marks an important step in the organization’s work to make information easier to find and improve collaboration across departments. Employees can access policies, procedures, departmental documentation, and other relevant resources in one place. This will reduce the time they spend searching for information, help teams work more efficiently, and support better-informed decisions.

Departments must keep their content accurate and current. The platform’s success depends on that upkeep. As the organization grows and changes, the knowledge base will remain a valuable resource for employees and help build a more connected, informed workplace.

### Human Writing

The new internal knowledge base is an important step in the organization’s ongoing work to make information easier to find and improve collaboration across departments. It gives employees a central place to access policies, procedures, departmental documentation, and other relevant resources. This will reduce the time employees spend searching for information and help teams work more efficiently and make better-informed decisions. The platform’s success will depend on departments keeping their content accurate and up to date. As the organization grows and evolves, the knowledge base will remain a valuable resource for employees, supporting their work and helping create a more connected and informed workplace.

### Prosen

The new internal knowledge base gives employees a central place to find policies, procedures, departmental documentation, and other relevant resources. It advances the organization’s ongoing efforts to make information easier to access and improve collaboration across departments. The platform will reduce the time employees spend searching for information, help teams work more efficiently, and support better-informed decisions. Its success will depend on departments keeping their content accurate and up to date. As the organization grows and evolves, the knowledge base will continue to support employees and help create a more connected and informed workplace.

</details>

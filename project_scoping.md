## Project Scoping & Data Ethics

I am a Data Analyst working for the Department for Business and Trade

**The Business Question & Hypothesis**:

    Question: What is the quantifiable economic impact of Regional Trade Agreements (RTAs), and how can we use this valuation to prioritize diplomatic and departmental resources for future negotiations?

    The Hypothesis: I hypothesize that RTAs act as a significant multiplier for trade flow, overcoming natural geographic and cultural frictions. My expectation is that the model will isolate and quantify an "RTA premium" (a measurable percentage or dollar-value boost to trade), proving that trade agreements generate specific, predictable economic returns.

**Relevance to Organisation**:

    Why does my department care? Negotiating a Regional Trade Agreement takes massive departmental resources spanning years of travel, legal drafting and economic analysis. Senior leaders needs to know if the effort is worth it.

    Model Application: By building a model that predicts bilateral trade based on gravity variables (GDP, distance, language) can we simulate "what-if" scenarios? We can input two countries that currently do not have an RTA, flip the RTA variable to "1" (True), and see the projected dollar increase in trade and by how much. This allows DBT to calculate the projected ROI of diplomatic efforts and prioritize negotiations with countries that offer the highest untapped potential.

## Ethics & Privacy:

**Privacy Concerns**: The CEPII dataset utilizes aggregated macroeconomic data at the national level. Because it contains no Personally Identifiable Information, there are no individual privacy risks or data protection regulations (like GDPR) violated in this analysis.

**Ethical Concerns & Biases**:

    Reporting Bias: Developed nations have highly funded statistical agencies that accurately track trade. Many developing nations have underfunded agencies, leading to missing data, under-reported GDPs, or a reliance on informal economies that aren't captured in official metrics.

    Policy Implications: If DBT uses an algorithm trained on biased data to allocate diplomatic resources, the model might systematically undervalue emerging economies. This could lead to a negative feedback loop where developing nations are ignored for future trade agreements simply because their historical data was poor. We will document this limitation, ensuring policymakers understand the model is a tool for augmentation, not absolute decision-making, and that diplomatic strategy must also weigh human rights and geopolitics, not just model outputs.
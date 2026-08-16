# Literature Review — Section 3: Summary and Synthesis
### (Person 2 — Literature Analyst) · AI Personal Coach · AI in Marketing Capstone

> **Note on structure.** The submission guidelines explicitly warn against listing papers one by one. This section is therefore written as four thematic narratives that compare sources against each other. The per-source metadata required by the brief (objective / data / method / findings / marketing contribution) is carried by the comparison matrix in §3.5, so no information is lost by avoiding a paper-by-paper list.
>
> **Marketing frame used throughout** (locked in `00_project_brief.md`): the paying customer is the parent of an LGS/YKS candidate; the end user is the student; the primary KPI is 90-day parent retention on a monthly subscription. Every source below is read through the question *what does this tell us about acquiring, engaging, and retaining that parent?*

---

## 3.1 Theme 1 — Behavioural segmentation as a marketing capability

The starting premise of our project is that two students preparing for the same exam disengage for different reasons, and that a subscription product must detect *which* reason applies before it can say anything useful. The segmentation literature supports this premise but also shows where it usually stops short.

Dullaghan and Rozaki (2017) segment mobile telecommunications customers using decision-tree induction (C5.0) combined with naïve Bayesian modelling, drawing on billing records and socio-demographic attributes. Their explicit motivation is commercial: identify behavioural profiles so that retention spending can be allocated where it changes an outcome rather than spread evenly. The paper is useful to us less for its algorithm than for its framing — segmentation is treated as a cost-allocation problem for marketing, not as an end in itself. Its limitation is equally instructive: the features are transactional (billing, tenure, plan type) and static, so the segments describe *what kind of customer* someone is rather than *what state they are in this week*.

Kuzilek, Hlosta, and Zdrahal (2017) provide the counterweight. Their Open University Learning Analytics Dataset (OULAD) links demographics, registration records, assessment results, and fine-grained virtual learning environment (VLE) clickstream traces for roughly 32,000 enrolments across seven course modules. The analytical unit is the enrolment — a student–module–presentation triple — which means the dataset natively supports *temporal* behavioural description: a learner's engagement can be traced week by week rather than summarised once. For our project this is the closest available proxy to a study routine log, and it is the reason OULAD was selected over generic marketing churn datasets (see the Data Research document for the full justification).

Read together, these two sources define the gap our segmentation approach targets. Telecommunications-style segmentation gives us the marketing logic (differentiated treatment, differentiated spend) but static features; learning analytics gives us behavioural granularity but is framed around institutional intervention rather than a paying customer. Our five sub-segments — *cannot start, abandons midway, phone-distracted, anxiety-driven procrastinator, night-shifted* — are an attempt to combine the two: behavioural and time-varying like OULAD, but tied to a differentiated message and a retention decision like the telecom work.

---

## 3.2 Theme 2 — Churn prediction and at-risk detection

Our project treats student disengagement and parent churn as two ends of the same causal chain: if the student stops working, the parent stops seeing value, and the subscription lapses. The literature on both ends converges on a similar set of findings.

Bello, Ajibade, and Ekweli (2025) evaluate machine learning models for churn in subscription businesses using a 7,043-customer dataset with 21 features. Random Forest and a boosting model both reached roughly 79% accuracy with AUC around 0.83, with the boosting model achieving slightly better recall on the churn class. Three of their findings matter for us. First, tenure, contract type, and monthly charges dominated feature importance — that is, churn was driven mostly by commercial and lifecycle variables rather than by engagement behaviour, which is precisely the blind spot our product tries to fill. Second, they report severe class imbalance, with non-churners heavily outnumbering churners, which is a design constraint we inherit. Third, and most directly relevant, they note that the literature they survey largely relies on static snapshots from telecom and banking without modelling time-dependent lifecycle behaviour, which limits the ability to detect early warning signs in time to intervene.

Jha, Ghergulescu, and Moldovan (2019) attack the same early-warning problem from the education side, applying ensemble, deep learning, and regression techniques to OULAD. Models built on students' VLE interaction achieved AUC of up to 0.91 for dropout prediction and 0.93 for final result prediction. The contrast with Bello et al. is the substantive finding of this theme: behavioural interaction data outperforms demographic and contractual data for predicting disengagement, and it does so at a horizon early enough to act on.

The comparison also exposes a shared limitation. Both literatures optimise for classification metrics — accuracy, AUC, F1 — and stop there. Neither measures whether the prediction changed anything. A model that identifies an at-risk student with AUC 0.91 and then produces a message the parent ignores has not moved a marketing KPI. This is the evaluation gap our capstone is positioned against, and it is why our brief specifies action-completion rate and 90-day retention as outcome measures alongside model AUC.

---

## 3.3 Theme 3 — Personalization and recommender systems

If segmentation tells us who someone is and churn models tell us when they are at risk, personalization is the layer that decides what they see. The evidence here is strong on effectiveness and unusually strong on the conditions under which effectiveness reverses.

Gomez-Uribe and Hunt (2016) describe Netflix's recommender architecture and, importantly for a marketing document, its business value: personalization is presented as a retention mechanism, with recommendation quality tied directly to subscriber lifetime rather than to a single conversion event. This is the mental model our project needs — for a subscription product, personalization is not a conversion tactic, it is the retention engine.

Matz, Teeny, Vaid, Peters, Harari, and Cerf (2024) test the mechanism experimentally. Across four studies comprising seven sub-studies with a combined N of 1,788, messages generated by ChatGPT and matched to a recipient's psychological profile were significantly more influential than non-personalized messages. The effect held across consumer marketing and political appeals, across different profiling dimensions (personality traits, political ideology, moral foundations), and — critically for a small team with no fine-tuning budget — even when the model received only a short prompt naming the target dimension. This is the single most relevant technical finding in our review: LLM-based tone and content adaptation is achievable through prompt design alone.

Hackenburg and Margetts (2024) are the necessary corrective. Using a custom application that injected self-reported demographic and political data into GPT-4 prompts in real time, they found that microtargeted messages did *not* hold a persuasive advantage over well-crafted non-targeted messages. The authors themselves suggest that returns to personalization may be larger in longer, multi-turn interactions where the model has more room to use what it knows. Placed against Matz et al., the honest reading of the literature is not "personalization works" but rather: personalization on *psychological and behavioural* dimensions shows measurable gains, personalization on *demographic* dimensions may not, and single-shot messages leave much of the potential unrealised. Our design responds to this directly — we personalize on observed behaviour and survey-elicited motivational profile rather than demographics, and the parent relationship is longitudinal rather than single-shot.

Aguirre, Mahr, Grewal, de Ruyter, and Wetzels (2015) supply the constraint that governs the whole design. Their studies on the personalization paradox show that more personalized advertising raises click-through when data collection is overt, but that covert collection increases consumers' feelings of vulnerability and depresses click-through instead. They further show that trust-building cues — signalling data practices, placing the message in a trusted context — can offset the negative effect. For a product that monitors a minor's phone during study blocks and reports to a parent, this is not a peripheral caveat. It is the reason our monitoring is scoped to the focus block only, why educational applications generate no alert, and why the data practice is disclosed rather than buried. Aguirre et al. reframe that decision from an ethical concession into a measurable marketing variable.

---

## 3.4 Theme 4 — Nudges, notification timing, and message framing

The final theme addresses the delivery mechanism itself: an automated message to a parent about their child's behaviour.

Bergman and Chan (2021) provide the strongest causal evidence available for our exact intervention. In a field experiment across 22 middle and high schools, weekly automated text alerts informed parents about missed assignments, grades, and absences. The alerts reduced course failures by 27%, increased class attendance by 12%, and increased student retention in the district, with larger effects for below-median-GPA students and high schoolers. There was no effect on state test scores. Two details deserve emphasis. First, more than 32,000 messages were sent at a variable cost of $63 — the intervention is cheap to run at scale, which is what makes a consumer subscription version economically plausible. Second, the mechanism the authors identify is informational: the alerts changed parents' beliefs about their child's performance and increased parental monitoring. Our weekly parent report is a direct commercial descendant of this design.

Kim, Kim, and Choi (2025) move from schools to app marketing. In a company-run field experiment with 595 users of an activity-monitoring app, tailored push notifications produced significantly higher engagement than generic ones, and notifications incorporating multiple personal identifiers outperformed those using a single identifier. Adding the user's own engagement history further improved engagement, though not significantly beyond name-based personalization alone. The practical lesson for our notification design is that a large share of the personalization benefit is captured by relatively shallow tailoring — useful for a two-month MVP that cannot afford a sophisticated targeting model at launch.

Vasquez, Patall, Fong, Corrigan, and Pine (2016) explain why the *framing* of these messages, not just their timing, determines whether they work. Their meta-analysis of 36 studies found that parental autonomy support was associated with greater academic achievement and with adaptive psychosocial outcomes including autonomous motivation, perceived competence, engagement, and positive attitudes toward school, with the strongest relation appearing for psychological health. The complementary literature on psychologically controlling parenting associates it with the opposite pattern. This is the empirical basis for our tone-transformation feature: converting a parent's controlling phrasing into autonomy-supportive phrasing is not a cosmetic softening, it is a shift toward the communication style that the evidence associates with better outcomes.

The tension across this theme is worth naming. Bergman and Chan show that informing parents works. Vasquez et al. show that how parents then act on that information determines whether it helps or harms. An alerting product that improves parental monitoring while degrading the parent–child interaction could raise short-term engagement and lower long-term retention. Our tone-transformation layer exists at precisely this junction, and it is the feature that most clearly distinguishes our project from a conventional parental monitoring app.

---

## 3.5 Comparison matrix

| Source | Data / context | Method | Reported metric | Marketing context | Key limitation for us |
|---|---|---|---|---|---|
| Dullaghan & Rozaki (2017) | Mobile telecom billing + socio-demographics | C5.0 decision tree, naïve Bayes | Segment-level classification | Retention spend allocation | Static transactional features; no temporal state |
| Kuzilek et al. (2017) | OULAD: ~32k enrolments, demographics, assessments, VLE clickstream | Dataset description / benchmark resource | — (resource paper) | None — institutional framing | No pricing, subscription, or customer variables |
| Bello et al. (2025) | 7,043 subscription customers, 21 features | Random Forest, boosting; imbalance handling | ~79% accuracy, AUC ≈ 0.83 | Subscription churn & retention targeting | Static snapshot; tenure/contract dominate over behaviour |
| Jha et al. (2019) | OULAD | Ensemble, deep learning, regression | AUC up to 0.91 (dropout), 0.93 (result) | None — education framing | No intervention outcome measured |
| Gomez-Uribe & Hunt (2016) | Netflix production system | Industrial recommender architecture | Business value, subscriber retention | Personalization as retention engine | Proprietary scale; not reproducible by a student team |
| Matz et al. (2024) | 4 studies, 7 sub-studies, N = 1,788 | LLM-generated profile-matched messages, RCT | Significant lift vs. non-personalized | Consumer marketing, political appeals | Short-horizon lab-style outcomes, not retention |
| Hackenburg & Margetts (2024) | Large randomized experiment, GPT-4 live prompting | Demographic/political microtargeting vs. generic | No persuasive advantage from targeting | Political persuasion | Single-turn only; demographic (not behavioural) targeting |
| Aguirre et al. (2015) | Experiments + Facebook CTR data | Overt vs. covert collection manipulation | CTR, perceived vulnerability | Personalized advertising | Advertising context, not ongoing service relationship |
| Bergman & Chan (2021) | 22 schools; 32,000+ messages, $63 variable cost | RCT, weekly automated alerts | −27% course failures, +12% attendance | Parent-facing automated messaging | Free institutional service, not a paid subscription |
| Kim et al. (2025) | 595 app users, company-run field experiment | Personalized vs. generic push, factorial | Engagement lift | App engagement marketing | Small N; low-stakes domain |
| Vasquez et al. (2016) | Meta-analysis, 36 studies | Correlational meta-analysis | Association with achievement & motivation | Message framing rationale | Correlational; no messaging-product evidence |

---

## 3.6 Synthesis: what the literature collectively shows

Four claims are supported well enough to build on.

**Behavioural signals beat demographic and contractual ones for predicting disengagement.** The AUC gap between the OULAD interaction-based models and the subscription churn models built on tenure and contract type is the clearest quantitative evidence in this review, and it justifies our decision to build the risk score on routine and focus-block behaviour.

**Automated parent messaging causally improves student outcomes and is cheap at scale.** Bergman and Chan remove the main feasibility doubt about our core loop. What their work does not establish is willingness to pay, because their intervention was delivered free by schools — a gap our project addresses by testing the same mechanism as a consumer subscription.

**LLM personalization delivers real gains, but the axis of personalization matters more than the fact of it.** Matz et al. and Hackenburg and Margetts only appear to contradict each other. Read together, they indicate that behavioural and psychological tailoring in a sustained relationship is where the returns lie, and that demographic tailoring in a single message is where they do not.

**Perceived surveillance can invert the benefit of personalization.** Aguirre et al. establish this as a measurable effect on click-through, not merely as an ethical worry. For a product that monitors a minor, disclosure and narrow scoping are retention features.

Two things the literature does **not** yet provide, which together define our contribution. First, no study in this review measures whether an AI-generated message actually changed a downstream behaviour and, through it, a retention metric — the field optimises AUC and stops. Second, the parent-messaging literature treats the parent as a passive recipient of information; none of it examines transforming the parent's *own* intended message before it reaches the child, which is the feature at the centre of our project. Section 4 develops both gaps.

---

## 6. Proper Citations

Aguirre, E., Mahr, D., Grewal, D., de Ruyter, K., & Wetzels, M. (2015). Unraveling the personalization paradox: The effect of information collection and trust-building strategies on online advertisement effectiveness. *Journal of Retailing, 91*(1), 34–49. https://doi.org/10.1016/j.jretai.2014.09.005

Bello, A.-W., Ajibade, I., & Ekweli, D. (2025). Predicting customer churn in subscription-based businesses using machine learning. *International Journal of Science and Research Archive, 16*(3), 1024–1038. https://doi.org/10.30574/ijsra.2025.16.3.2664

Bergman, P., & Chan, E. W. (2021). Leveraging parents through low-cost technology: The impact of high-frequency information on student achievement. *Journal of Human Resources, 56*(1), 125–158. https://doi.org/10.3368/jhr.56.1.1118-9837R1

Dullaghan, C., & Rozaki, E. (2017). *Integration of machine learning techniques to evaluate dynamic customer segmentation analysis for mobile customers* (arXiv:1702.02215). arXiv. https://arxiv.org/abs/1702.02215

Gomez-Uribe, C. A., & Hunt, N. (2016). The Netflix recommender system: Algorithms, business value, and innovation. *ACM Transactions on Management Information Systems, 6*(4), Article 13. https://doi.org/10.1145/2843948

Hackenburg, K., & Margetts, H. (2024). Evaluating the persuasive influence of political microtargeting with large language models. *Proceedings of the National Academy of Sciences, 121*(24), e2403116121. https://doi.org/10.1073/pnas.2403116121

Jha, N. I., Ghergulescu, I., & Moldovan, A.-N. (2019). OULAD MOOC dropout and result prediction using ensemble, deep learning and regression techniques. In *Proceedings of the 11th International Conference on Computer Supported Education (CSEDU 2019)* (pp. 154–164). SCITEPRESS. https://doi.org/10.5220/0007767601540164

Kim, J., Kim, W., & Choi, J. (2025). Push the paw: A field experiment on personalised push notifications and user engagement. *Australasian Marketing Journal*. Advance online publication. https://doi.org/10.1177/14413582251356702

Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data, 4*, 170171. https://doi.org/10.1038/sdata.2017.171

Matz, S. C., Teeny, J. D., Vaid, S. S., Peters, H., Harari, G. M., & Cerf, M. (2024). The potential of generative AI for personalized persuasion at scale. *Scientific Reports, 14*, 4692. https://doi.org/10.1038/s41598-024-53755-0

Vasquez, A. C., Patall, E. A., Fong, C. J., Corrigan, A. S., & Pine, L. (2016). Parent autonomy support, academic achievement, and psychosocial functioning: A meta-analysis of research. *Educational Psychology Review, 28*(3), 605–644. https://doi.org/10.1007/s10648-015-9329-z

---

## TODO before pushing

- [ ] **Verify every citation yourself.** Open each DOI and confirm authors, year, volume, and page numbers. Two entries need a closer look: the Jha et al. CSEDU DOI, and the Kim et al. article, which was published online ahead of its journal issue — check whether a final volume/issue has since been assigned.
- [ ] **Add 1–2 Turkish-context sources.** Nothing here is about LGS/YKS, Turkish parents, or the Turkish private tutoring market. Even one paper or a TÜİK/MEB report on exam-prep spending would strengthen §3.1 and give Person 1 something concrete for the gap section. Check DergiPark and YÖK Tez.
- [ ] **Send Person 1 the two-sentence gap summary** from the end of §3.6 — that is the input for LR §4, and they are blocked until they have it.
- [ ] **Send Person 5 the Matz, Hackenburg, and Aguirre entries** — those three carry directly into Technology Review §4 and §6 and should not be researched twice.
- [ ] **Merge these entries into `references.bib`** rather than leaving them only in this file.
- [ ] Read once for length: this is roughly 4–5 pages. If it needs trimming, cut §3.1 rather than §3.4 — theme 4 carries the strongest causal evidence.

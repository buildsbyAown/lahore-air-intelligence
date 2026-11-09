# What would actually lower Lahore's smog?

*Lahore Air Intelligence — mitigation note, November 2026*

The forecast in this project predicts tomorrow's PM2.5 if the city keeps emitting as it does now. This note is the other half of the study: which of the controls people ask for can reduce the problem, and which physical setting each one needs. I cover the three that were requested — room air purifiers, cleaners on vehicle exhausts, and cleaners at the mouths of brick kilns — and I apply the same test to the other large particle sources already in the literature review.

I only use numbers from the project data or from sources listed at the end. Where a percentage comes from a paper, it is the paper's result for that device or that kiln, not a prediction of Lahore's city-wide concentration.

## The test a control has to pass

A filter removes particles from the air that passes through it. That helps when the air is enclosed long enough for the machine to treat it:

- a room, with the door and windows mostly shut;
- a tailpipe, where all of that vehicle's exhaust goes through one duct;
- a kiln chimney, where the flue gas goes through one stack.

The same filter, stood in a street or a park, treats a trickle of air while the wind replaces the city's air and the sources keep emitting. Outdoor "smog towers" fail that test. Guttikunda and Jawahar (2020) put it directly for Delhi: the airshed has no walls, so vacuuming outdoor air and releasing it back into the same air does not clean the city [1]. Delhi's own pollution-control committee later told the National Green Tribunal that the towers' measured effect was about 13–15% within 200 m, against a design claim of 1 km [2].

Lahore's winter lid does not change this. In the project data, the night-time boundary layer in November–January averages **53 m** (median 38 m, 399 days). Consider a footprint of 40 km by 40 km, which is the order of Lahore District, a 50 m lid, and the winter mean wind in the same data, **6 km/h**:

- air flowing through that box ≈ 40,000 m × 50 m × 6,000 m/h = **1.2 × 10¹⁰ m³ every hour**;
- a large demonstration tower, the 10 million m³/day scale used in the Delhi calculation [1], treats about **4 × 10⁵ m³/h**;
- one such tower therefore treats about **0.003%** of the air moving through the city;
- matching that flow once would take on the order of **30,000** towers, while kilns, vehicles and fires kept adding particles inside the box.

The exact area can be twice as big or half as big and the conclusion is the same. A shallow boundary layer makes each kilogram of emissions *more concentrated*. It does not turn the city into a room that one machine can filter. The forecast's main weather signal — the night-time boundary layer collapsing — is a reason to cut emissions and to protect people indoors on those days. It is not a reason to build outdoor purifiers.

## 1. Room air purifiers (HEPA)

**What they change.** The concentration in the room where the machine runs.

**What they leave alone.** The outdoor air, the street, and every room that does not have a machine.

Portable HEPA cleaners do reduce indoor PM2.5 when they are sized for the room and the room is closed. A review of portable purifiers in homes, schools and offices found indoor PM2.5 reductions between **22.6% and 92%** across the studies it included [3]. A second review of real-world personal filtration found reductions of about **11% to 82%** [4]. The US EPA's summary of home studies is "on the order of approximately 50 percent or higher" for high-efficiency portable cleaners [5]. A classroom trial in Los Angeles measured **39.9%** lower school-year PM2.5 with portable HEPA units, in a year when outdoor PM2.5 was only about 8–10 µg/m³ [6]. Another school trial found a **32%** indoor reduction and fewer absences; the effect on absences was smaller when outdoor pollution was higher [7].

None of those trials is Lahore. This project has no indoor measurements, so I do not claim a Lahore reduction. The honest use of the monitor record is to show the outdoor level a purifier would be fighting.

On the 1,456 valid consulate days (23 May 2019–17 Feb 2025):

| Period | Valid days | Mean PM2.5 | Share above 15 µg/m³ (WHO 24-h) | Share above 150.4 | Share above 250.4 |
|---|---:|---:|---:|---:|---:|
| All measured days | 1,456 | 132 | 99.5% | 32% | 14% |
| November–February | 526 | 230 | 100% | 76% (398 days) | 37% (196 days) |

November–February holds **63%** of the sum of daily means, and **86%** of the days above 150.4 µg/m³. That is the season when a purifier programme would run. On those 398 November–February days above 150.4, the outdoor mean was **266 µg/m³**. If a closed room started at that outdoor level and a purifier then held a reduction in the published range:

| Indoor reduction, if the room starts at 266 | Indoor PM2.5 |
|---:|---:|
| 30% | 186 |
| 50% | 133 |
| 70% | 80 |

All three are still many times the WHO 24-hour guideline of 15 µg/m³. A purifier in a Lahore winter is harm reduction for the people inside that room. It is not a way to make the air safe, and it does nothing for anyone outside. It only holds those reductions if the machine is big enough for the room (the usual rule is a clean-air delivery rate that replaces the room's air several times an hour), the windows stay mostly shut, and the filter is replaced when it loads up. Lahore's winter cold helps the "windows shut" condition. An open window, or a machine that is off, removes the benefit.

**How this connects to the forecast.** Random Forest [A] caught 93% of Very Unhealthy days in the test set and can be issued from data that already exist (see [`model_assessment.md`](model_assessment.md)). That flag is a switch for schools, hospitals and homes: run the purifiers, keep windows closed, move sport indoors. The flag does not lower the outdoor number.

## 2. Cleaners on vehicle exhausts

**What belongs on an exhaust.** An aftertreatment device in the tailpipe, through which that vehicle's exhaust is forced to pass.

- A **diesel particulate filter (DPF)** traps the solid particles. Reviews put the removal at about **85%**, and often **above 90–95%**, of diesel particulate matter when the filter is the right one for the engine and it stays on the vehicle [8, 9].
- A **diesel oxidation catalyst** burns a share of the soluble organic particles, hydrocarbons and carbon monoxide. It is not a substitute for a DPF on the solid soot.
- A **three-way catalytic converter** is the petrol-car device. It cuts carbon monoxide, nitrogen oxides and hydrocarbons. Motorcycles need a working catalyst too. A DPF is a diesel device; fitting one to a petrol motorcycle is the wrong machine.

**The fuel decides whether the filter survives.** DPFs and the catalysts that help them regenerate are specified for low-sulfur diesel, below 50 ppm and preferably at or below 10 ppm [10]. Pakistan ordered imported petrol and diesel to meet Euro-V specifications, sulfur no more than 10 ppm, with diesel imports under that rule from **1 January 2021** [11]. PSO launched a Euro-5 diesel and described the sulfur cut as 500 ppm to 10 ppm [12]. The same government decision recorded that local refineries could not then produce that grade, so fuel sold in parts of the country could remain the older product [11]. A DPF programme for Lahore buses and trucks therefore needs the fuel that is actually in the tank to be the 10 ppm grade, plus an inspection system so filters are not removed. High-sulfur fuel poisons the catalyst and clogs the filter. The device then gets taken off, and the emission cut disappears.

**How large a share of Lahore's PM2.5 this can touch.** The Urban Unit inventory is easy to misread, and the literature review already flags it [13]. "Transport is 83%" is the share of *all pollutants added together*, and that total is mostly carbon monoxide from motorcycles and cars. In the same report's primary PM2.5, transport is 397 tonnes, crop-residue burning 371 tonnes, waste burning 320 tonnes, and industry 29 tonnes. Exhaust particle filters attack the transport line of that table, plus the secondary particles that form from vehicle gases, which the inventory does not count. They do not, on these figures, remove most of the directly emitted PM2.5. Crop and waste burning are about as large in that primary-PM table.

Stone and colleagues' 2007 chemical study in Lahore attributed **53%** of primary organic carbon in PM2.5 to non-catalysed motor vehicles, with a further unexplained share they linked to coal and, probably, brick kilns [14]. That is an old fingerprint, and it is a share of one component of the particles, not of total PM2.5 mass. It is still the reason exhaust controls belong in the study: a large part of the carbon in Lahore's fine particles has looked like poorly controlled vehicles.

I am not converting 397 tonnes, or 53%, into a city-wide µg/m³ forecast. Secondary particles, dust, and pollution blown in from outside the district are not in that arithmetic. The World Bank's South Asia assessment is that less than half of the pollution in the region's major cities is produced inside the city [15].

## 3. Cleaners at brick-kiln mouths

**What works at a kiln.** Two different changes, both at the kiln, and they should not be confused with a room purifier bolted over the firing hole.

**First, burn the fuel properly.** A conventional fixed-chimney Bull's trench kiln burns coal, rice husk, bagasse and wood inefficiently. Bashir and colleagues at UET Lahore compared that kiln with induced-draught zigzag firing and estimated about **35% less PM2.5**, about **30% less CO₂**, and a large cut in black carbon, together with about 30% less energy per brick [16]. A Punjab EPA stack study of four kilns (one of them a high-draught zigzag at Raiwind, Lahore) found the same ranking when the zigzag was actually built to the design, and the opposite ranking when a kiln had been relabelled zigzag without following the design manual: an improper conversion emitted more, not less [17]. That paper's sample is four kilns on one day each. Its useful conclusion is operational: the province should check the design and the Punjab Environmental Quality Standard for particulate matter (500 mg/Nm³), because a zigzag name on the gate is not a measurement. A later Punjab EPA estimate, built from emission factors rather than from Lahore's air monitor, put the brick sector's particulate emissions about **29%** lower by December 2024 than in a 2019 all-traditional baseline, after enforcement of zigzag adoption [18]. The consulate winter series in this project does not show a matching decline in ambient PM2.5. Both can be true: a kiln-sector cut can be real and still be too small, or too far from this one monitor, to move the city concentration this dataset records.

**Second, clean the flue that remains.** Once the gas is inside the chimney it can be passed through a real stack device.

- A **cyclone** or a settling chamber drops coarse grit. PM2.5, the size that defines the smog, mostly stays in the gas. A screen or a household purifier over the kiln mouth fails in the same way, and it also fails mechanically: the flue is hot, tarry, wet and far too large a volume for a room-sized fan.
- A **wet scrubber** is a genuine stack device and is often what people mean by a cleaner on the chimney. On coarse particles it can remove a large share. On the submicron particles that dominate PM2.5 health risk it is weak: a field study of a spray scrubber on a biomass boiler found almost complete removal above 1 µm and only **26–36%** removal below that [19]. That is a boiler, not a Lahore kiln. It is the right order of magnitude to keep in mind so a scrubber is not described as a 99% PM2.5 solution.
- A **fabric filter (baghouse)** or an **electrostatic precipitator** is the device class that removes the large majority of particle *mass* from an industrial flue, including fine particles, in standard emissions practice. On a traditional Punjab kiln they need electricity, temperature control, ash handling and maintenance that the kiln often does not have. They are the honest "cleaner on the mouth" if the goal is the fine particles. They are a project, not a filter cloth.

The Urban Unit counts about **230 brick kilns** in Lahore District and describes them as major coal users on the city's edge [13]. Its industry line for primary PM2.5 is only 29 tonnes, which sits awkwardly next to Stone and colleagues' coal-marker result [14]. I leave that conflict as a conflict. Kiln controls are justified because the kilns are a known, local, coal-burning source that can be rebuilt and measured at the stack. They are not justified by pretending the inventory has already proved they are the main source of the city's PM2.5.

## 4. The other sources the same test points to

Exhaust filters and kiln stacks leave two primary-PM lines in the Lahore inventory that are each about as large as transport: crop-residue burning and waste burning [13]. FAO's provincial inventory ranks transport, industry, then agriculture, and still treats the October–November burning peak as important because it is concentrated in a few weeks [20]. This project's fire series agrees with the seasonal part and refuses the "fires explain winter" part: October–November detections fell sharply after 2021 while winter PM2.5 did not. A control on stubble (machinery that lets farmers sow without burning, in the short window between rice and wheat) and a control on waste (collection, so it is not burned in the street) act at the source, which is where a cut in emissions actually changes outdoor concentrations. They belong in any programme that also funds filters and kilns. Otherwise the city can retrofit chimneys and still fill with smoke in November.

## What I will not claim

- I will not publish a single "% less outdoor smog in Lahore" that adds purifiers, exhaust filters and kiln scrubbers together. Personal-exposure scenarios and inventory shares are calculated separately in [`technology_risk_reduction.md`](technology_risk_reduction.md). The forecast model cannot produce a city-concentration scenario, and the inventories do not include secondary particles or the regional share.
- Room purifiers do not appear in the outdoor time series. Buying them will not make the consulate monitor fall.
- A device helps only while it is operated. A zigzag kiln run off the design, a DPF removed because the fuel is wrong, and a school purifier with a clogged filter are all zero.

## How the forecast and the controls fit together

| Job | Tool in this study |
|---|---|
| Tomorrow's PM2.5 at the monitor, emissions unchanged | Random Forest [A] now; Random Forest [B] after a real weather forecast is tested |
| When to close windows, cancel outdoor sport, and run room purifiers | The same forecast's Very Unhealthy flag (93% of those days caught in the test) |
| Lower outdoor PM2.5 for the whole city | Emission cuts at the duct or at the fire: DPF and catalysts on a low-sulfur fuel, zigzag kilns that meet the stack standard, flue filters where the kiln can run them, and less open burning of residue and waste |
| Outdoor purifiers and smog towers | Ruled out at city scale by the volume of air moving through the winter boundary layer |

After a real, city-scale emission change, the Random Forest has to be retrained. It learned the emission level of 2019–2025. It will keep predicting that level until the new measurements are in the training data.

## References

1. Guttikunda, S., & Jawahar, P. (2020). Can we vacuum our air pollution problem using smog towers? *Atmosphere*, 11(9), 922. https://doi.org/10.3390/atmos11090922
2. Delhi Pollution Control Committee, as reported by *The Indian Express* (9 November 2023), "Smog towers not solution to air pollution: DPCC to NGT." https://indianexpress.com/article/cities/delhi/smog-towers-not-solution-air-pollution-dpcc-ngt-9031142/
3. Cheek, E., Guercio, V., Shrubsole, C., & Dimitroulopoulou, S. (2021). Portable air purification: Review of impacts on indoor air quality and health. *Science of the Total Environment*, 766, 142585. https://doi.org/10.1016/j.scitotenv.2020.142585
4. Zhu, Y., Song, X., Wu, R., Fang, J., Liu, L., Wang, T., Liu, S., Xu, H., & Huang, W. (2021). A review on reducing indoor particulate matter concentrations from personal-level air filtration intervention under real-world exposure situations. *Indoor Air*. https://doi.org/10.1111/ina.12922
5. US Environmental Protection Agency (2018). *Residential Air Cleaners: A Technical Summary*, 3rd edition. https://www.epa.gov/sites/default/files/2018-07/documents/residential_air_cleaners_-_a_technical_summary_3rd_edition.pdf
6. Simona, S. C., Bartell, S. M., & Vieira, V. M. (2025). Classroom air quality in a randomized crossover trial with portable HEPA air cleaners. *Journal of Exposure Science & Environmental Epidemiology*. https://www.nature.com/articles/s41370-025-00743-9
7. Resources for the Future. *The effect of air purifiers in schools* (working paper). https://www.rff.org/publications/working-papers/the-effect-of-air-purifiers-in-schools/
8. Castoldi, L. (2020). An overview on the catalytic materials proposed for the simultaneous removal of NOx and soot. *Materials*, 13(16), 3551. https://doi.org/10.3390/ma13163551 — "A DPF can remove around 85% of the particulates from the exhaust."
9. Dong, R., Zhang, Z., Ye, Y., Huang, H., & Cao, C. (2022). Review of particle filters for internal combustion engines. *Processes*, 10(5), 993. https://www.mdpi.com/2227-9717/10/5/993 — filtration efficiency of a DPF is usually higher than 95%, and DPFs can reduce more than 90% of diesel particles.
10. Climate and Clean Air Coalition. *Guidance for Fuel Importing Countries.* Diesel particulate filters "can reduce PM2.5 emissions up to 99%" and "are only effective with low (<50 ppm) or ideally ultralow (<10 ppm) sulfur fuels." https://www.ccacoalition.org/sites/default/files/resources/Guidance%20for%20Fuel%20Importing%20Countries_small.pdf — see also Dallmann, T., Shao, Z., et al., ICCT (2020), *Diesel sulfur content impacts on Euro VI soot-free vehicles.* https://theicct.org/sites/default/files/publications/50-ppm-sulfur-impacts-04.2020.pdf
11. *Dawn* (23 June 2020). "Govt orders all petrol, diesel imports be Euro-V compliant as oil companies protest move." Diesel imports to conform to Euro-V from 1 January 2021; sulfur not more than 10 ppm; local refineries could not produce that grade. https://www.dawn.com/news/1567870
12. Pakistan State Oil (31 December 2020). Launch of Euro 5 high-speed diesel; sulfur described as reduced from 500 ppm to 10 ppm. https://www.psopk.com/en/media/press-releases/another-first-by-pso-launch-of-euro-5-standard-diesel-in-pakistan
13. The Urban Unit, Planning & Development Board, Government of Punjab (2023). *Sectoral Emission Inventory of Lahore.* https://urbanunit.gov.pk/Download/publications/Files/8/2023/Emission%20Inventory%20of%20Lahore%202023.pdf
14. Stone, E., Schauer, J., Quraishi, T. A., & Mahmood, A. (2010). Chemical characterization and source apportionment of fine and coarse particulate matter in Lahore, Pakistan. *Atmospheric Environment*, 44(8), 1062–1070. https://doi.org/10.1016/j.atmosenv.2009.12.015
15. World Bank (2022). *Striving for Clean Air: Air Pollution and Public Health in South Asia.* https://www.worldbank.org/en/region/sar/publication/striving-for-clean-air
16. Bashir, Z., Amjad, M., Raza, S. F., Ahmad, S., Abdollahian, M., & Farooq, M. (2023). Investigating the impact of shifting the brick kiln industry from conventional to zigzag technology for a sustainable environment. *Sustainability*, 15(10), 8291. https://doi.org/10.3390/su15108291
17. Sheikh, I. H., Naz, N., Nadeem, M., Hussain, F., Alam, M. F., Haider, R., & Javed, T. (2024). Comparison of emissions from different brick kiln technologies in Punjab, Pakistan. *Pakistan Journal of Science*, 76(3), 363–371. https://doi.org/10.57041/vol76iss03pp363-371
18. Punjab EPA enforcement estimate of brick-sector emissions after zigzag adoption: "Impact of EPA enforcement activities on emission reduction of brick kilns in Punjab." *Pakistan Journal of Science*. https://pjosr.com/index.php/pjs/article/view/1319 — sector inventory calculation, 29.32% lower particulate matter and 16.08% lower greenhouse gases from 2019 to December 2024, not a measurement of ambient PM2.5 in Lahore.
19. Field measurements of a centrifugal spray scrubber on a 3 MW biomass boiler: near-complete removal above 1 µm, 26–36% for submicron particles. Kyushu University record of the study: https://kyushu-u.elsevierpure.com/en/publications/field-measurements-and-stochastic-modeling-of-particle-removal-in/
20. FAO. *Remote sensing for space-time mapping of smog in Punjab and identification of the underlying causes using GIS (R-SMOG).* https://openknowledge.fao.org/server/api/core/bitstreams/ede8e081-5a05-4722-86e7-359e4be3dd6b/content

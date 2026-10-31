# Why is Lahore's air so polluted? A short literature review

*Lahore Air Intelligence — background brief, version 1 (November 2026)*

This brief summarises what published reports and peer-reviewed studies say about the causes of Lahore's smog. I only cite sources I have opened and read. For each, I note what kind of evidence it is, because "how big is a source" and "what conditions trap pollution" are different questions that need different evidence.

---

## 1. How bad is the problem?

- **Lahore is consistently among the most polluted cities in the world.** In IQAir's 2024 World Air Quality Report, Lahore's annual average PM2.5 was **102.1 µg/m³**, up from 86.5 µg/m³ in 2021 and 99.5 µg/m³ in 2023. IQAir describes Lahore as the most polluted city in the world in 2022 and says it has had hazardous-level air quality every year since 2017 [1]. That is about **20 times** the WHO annual guideline of 5 µg/m³ [2, 3].
- **Health cost.** The Air Quality Life Index (University of Chicago) estimates that people in Lahore would gain **5.8 years** of life expectancy if PM2.5 met the WHO guideline. For Pakistan as a whole the figure is 3.3 years, and particulate pollution is the country's biggest external threat to life expectancy. Pakistan relaxed its national annual PM2.5 standard from 15 to 35 µg/m³ in 2023 [3].
- **It is not new.** A year-long sampling campaign in 2007 measured an annual average PM2.5 of **194 ± 94 µg/m³** in Lahore [4], and another study reported 118 µg/m³ for Lahore for 2007 [5].
- **It is regional.** The World Bank's *Striving for Clean Air* (2022) reports that South Asia has 9 of the world's 10 cities with the worst air pollution, causing an estimated 2 million premature deaths a year. Pollution is trapped in large "airsheds" shaped by climate and geography, and **less than half of the air pollution in South Asia's major cities is produced within the cities** [6].

## 2. Where does the pollution come from? (Emission sources)

Two kinds of evidence exist for Lahore: **emission inventories** (estimate how much each sector emits) and **source apportionment** (chemically fingerprint the particles in the air). They answer slightly different questions.

### 2.1 Emission inventories

- **The Urban Unit (Government of Punjab), *Sectoral Emission Inventory of Lahore* (2023)** [7] — the first district-scale inventory in Punjab. It is widely quoted as saying **transport causes 83%** of Lahore's pollution (83.15% transport, 9.07% industry, 3.9% crop-residue burning, 3.6% waste burning, 0.14% commercial, 0.11% domestic).
  - **Something I noticed when reading the report itself:** the 83% is the share of the *total mass of all pollutants combined* (CO, NOx, NMVOC, SOx, TSP, PM10, PM2.5), and that total is dominated by **carbon monoxide** (101,820 of 110,987 tonnes) from motorcycles and cars. If you look only at **directly emitted PM2.5** in the same report's Table 3, the split is very different: transport 397 t, crop-residue burning 371 t, waste burning 320 t, industry 29 t. So for fine particles specifically, crop and waste burning are about as important as traffic in this inventory. (It also does not cover secondary particles formed in the air, or pollution blown in from outside the district.)
  - The report counts about **4,800 registered industries and 230 brick kilns in Lahore District** and notes that kilns are major coal users on the city's outskirts [7].
- **FAO R-SMOG study for Punjab province** [8] — for the whole province, transport 43%, industry 25%, agriculture (rice-residue burning) 20%, power 12% of total air-pollutant emissions. FAO notes crop burning is "only the third sector by air pollutant emissions" but is significant for the *seasonal* smog because it is concentrated in October–November. FAO recommends smog **monitoring and early-warning systems**.

### 2.2 Source apportionment (chemical fingerprinting)

- **Stone et al. (2010), *Atmospheric Environment*** [4] — the classic Lahore study (Jan 2007 – Jan 2008). Fine particles were dominated by carbon-containing material (61%). For primary organic carbon in PM2.5: **non-catalysed motor vehicles 53%**, biomass burning 10%, diesel/residual fuel oil 6%, coal 1.9%. A large unexplained share (27%) correlated with coal markers, and the authors suggest **brick kilns** (which burn coal and low-quality fuels) as the most probable source. Secondary organic aerosol was important in winter fog episodes.
- This is old data (2007). **A modern source-apportionment study for Lahore is a clear gap.**

### 2.3 Brick kilns

- Conventional fixed-chimney Bull's trench kilns burn low-quality coal with rice husk, bagasse and wood. A life-cycle study from UET Lahore [9] estimated that converting to **induced-draught zigzag kilns** would cut PM2.5 emissions by about **35%**, CO2 by about 30% and black carbon substantially. This is one of the few concrete, already-proven mitigation measures.

### 2.4 Crop-residue burning and regional transport

- The rice–wheat cycle leaves farmers only 10–20 days between harvesting rice and sowing wheat, so stubble is burned in Indian and Pakistani Punjab in October–November [10].
- Modelling across the Indo-Gangetic Plain shows that **biomass burning in the north-west plain plays a crucial role in the post-monsoon (Oct–Nov) peak**, while in mid-winter the problem shifts to stagnant weather trapping local emissions [11].
- For the record November 2024 episode, air-mass back-trajectories passed over the stubble-burning region, and fire activity shifted from afternoon to evening [10] — which matters because polar-orbiting satellites (MODIS) pass in the late morning and early afternoon and can miss evening fires.

## 3. Why does winter make it so much worse? (Meteorology and geography)

This is the part of the problem my own data analysis focuses on.

- **Shallow boundary layer / temperature inversion.** In winter the ground cools quickly at night, creating a temperature inversion: a warm layer sits on top of cold air near the ground and acts like a lid. Ceilometer (LIDAR) measurements in Lahore from Oct 2019 to Mar 2021 found the **planetary boundary layer was usually below 500 m in December**, and **PM2.5 rose when the boundary layer dropped** [12]. Older work cites night-time winter mixing heights of about 250 m [5].
- **Weak winds and stagnation.** Across the Indo-Gangetic Plain, the move into winter brings lower temperatures, a much shallower boundary layer and weaker winds; the **ventilation coefficient falls by a factor of about 4** [11]. The Himalaya along the north-east edge of the plain forms a corridor that helps aerosols accumulate over the region [11].
- **The November 2024 event.** Lahore recorded a daily PM2.5 of **621 µg/m³**, the highest in five years. A 2026 study links it to a prolonged high-pressure system (anticyclonic stagnation), weak winds, low boundary layer, higher humidity and fire activity — i.e. **many sources, trapped by weather** [10].
- **Fog and humidity** help turn gases into particles (secondary aerosol) during winter [4, 5].

## 4. Can computer science help? Previous forecasting work

- A 2026 study from the University of the Punjab [13] combined satellite data (MODIS aerosol optical depth, Sentinel-5P gases), ERA5 weather and ground measurements to predict daily PM2.5 in Lahore with Random Forest, XGBoost, LightGBM and CatBoost (trained on 2019–2023, tested on 2024). Random Forest reached **R² = 0.77, RMSE = 24.75 µg/m³**, and an ensemble did slightly better. Surface pressure, temperature, CO and NO2 were the most important inputs. The authors note that Lahore "still lacks reliable short-term PM2.5 forecasting systems."
- The meteorology papers above [10, 11] conclude that **emission controls should be guided by weather forecasts** — which is exactly what a short-term forecasting / early-warning system can support.

## 5. What this means for my project

1. **The research gap I can realistically work on is forecasting and early warning**, not source attribution. Source shares need inventories or chemical measurements, which I do not have.
2. The literature strongly suggests that **meteorology (boundary layer height, wind, stagnation) decides how bad a given day gets**, while emissions from traffic, kilns, industry, crop and waste burning provide the pollution. My first analysis tests the meteorology part with real data.
3. **Data is a real limitation**: one reference monitor, a few low-cost sensors, and models that underestimate Lahore. Calibrating low-cost sensors and modelled data is a useful CS/ML contribution in itself.
4. Headline numbers like "83% transport" need careful reading: they depend on which pollutants are counted.
5. **Controls are a separate question from the forecast.** A companion note, [`mitigation_options.md`](mitigation_options.md), goes through three ideas that come up in Lahore: room air purifiers, cleaners on vehicle exhausts, and cleaners at brick-kiln mouths. Filtration reduces particles where the air is enclosed (a room, a tailpipe, a chimney). It does not vacuum the outdoor air of the city. The next-day model predicts concentrations under today's emissions; it is not an estimate of those controls.

---

## References

1. IQAir. *5 Most polluted major cities in the world in 2024* (based on the 2024 World Air Quality Report). https://www.iqair.com/newsroom/5-most-polluted-major-cities-in-world-2024 — full report: https://mail.e3.iqair.com/hubfs/WAQR/2024_World_Air_Quality_Report.pdf
2. World Health Organization (2021). *WHO Global Air Quality Guidelines: Particulate Matter (PM2.5 and PM10), Ozone, Nitrogen Dioxide, Sulfur Dioxide and Carbon Monoxide.* https://iris.who.int/bitstream/handle/10665/345329/9789240034228-eng.pdf
3. Energy Policy Institute at the University of Chicago (EPIC). *Air Quality Life Index — Pakistan Fact Sheet (2025, 2023 data).* https://aqli.epic.uchicago.edu/files/Pakistan%20FactSheet_2025.pdf
4. Stone, E., Schauer, J., Quraishi, T. A., & Mahmood, A. (2010). Chemical characterization and source apportionment of fine and coarse particulate matter in Lahore, Pakistan. *Atmospheric Environment*, 44(8), 1062–1070. https://doi.org/10.1016/j.atmosenv.2009.12.015
5. Rasheed, A., et al. (2015). Measurement and analysis of fine particulate matter (PM2.5) in urban areas of Pakistan. *Aerosol and Air Quality Research*, 15, 426–439. https://airqualityresearch.wordpress.ncsu.edu/files/2019/08/6_AAQR-14-10-OA-0269_426-439.pdf
6. World Bank (2022). *Striving for Clean Air: Air Pollution and Public Health in South Asia.* Press release: https://www.worldbank.org/en/news/press-release/2022/12/14/urgent-action-needed-in-south-asia-to-curb-deadly-air-pollution — report page: https://www.worldbank.org/en/region/sar/publication/striving-for-clean-air
7. The Urban Unit, Planning & Development Board, Government of Punjab (2023). *Sectoral Emission Inventory of Lahore.* https://urbanunit.gov.pk/Download/publications/Files/8/2023/Emission%20Inventory%20of%20Lahore%202023.pdf
8. FAO (Food and Agriculture Organization). *Remote sensing for space-time mapping of smog in Punjab and identification of the underlying causes using GIS (R-SMOG).* https://openknowledge.fao.org/server/api/core/bitstreams/ede8e081-5a05-4722-86e7-359e4be3dd6b/content — news release: https://www.fao.org/pakistan/news/detail-events/en/c/1179183/
9. Bashir, Z., Amjad, M., Raza, S. F., Ahmad, S., Abdollahian, M., & Farooq, M. (2023). Investigating the impact of shifting the brick kiln industry from conventional to zigzag technology for a sustainable environment. *Sustainability*, 15(10), 8291. https://doi.org/10.3390/su15108291
10. Dahal, S., Sharma, N., Dey, S., Bokhari, S. A. A., Boomsma, J., …, & Holmes, H. A. (2026). Meteorological modulation of ambient air quality in Delhi and Lahore during the November 2024 haze event. *Scientific Reports*. https://www.nature.com/articles/s41598-026-63281-w
11. Ojha, N., Sharma, A., Kumar, M., Girach, I., Ansari, T. U., Sharma, S. K., Singh, N., Pozzer, A., & Gunthe, S. S. (2020). On the widespread enhancement in fine particulate matter across the Indo-Gangetic Plain towards winter. *Scientific Reports*, 10. https://www.nature.com/articles/s41598-020-62710-8
12. Shahid, I., & Shahzad, M. I. (2023). Impact of planetary boundary layer in dense haze/smog event over South Asian mega city; Lahore, Pakistan. *EGU General Assembly 2023*, EGU23-11384 (conference abstract). https://doi.org/10.5194/egusphere-egu23-11384
13. Haseeb, M., Tahir, Z., Mehmood, S. A., Arif, H., Kousar, S., Ghafoor, S., & Mehmood, K. (2026). Ensemble artificial intelligence fusing satellite, reanalysis, and ground observations for improved PM2.5 prediction. *Atmosphere*, 17(4), 411. https://www.mdpi.com/2073-4433/17/4/411

*Data sources used in the analysis are listed separately in `data/README.md`.*

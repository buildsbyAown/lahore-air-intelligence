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

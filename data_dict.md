Variables  
• *country_id*: country identifier, unilateral.  
• *iso3*: ISO3 alphabetic code, unilateral.  
• *iso3num*: ISO3 numeric code, unilateral.  
• *countrygroup_iso3*: Largest entity of which the country was/is part of (ISO3 alphabetic
code), unilateral.  
• *countrygroup_iso3num*: Largest entity of which the country was/is part of (ISO3 nu-
meric code), unilateral.  
• *country*: Country name, unilateral.  
• *countrylong*: Country official name, unilateral.  
• *first_year*: First year of territorial existence, unilateral.  
• *last_year*: Last year of territorial existence, unilateral.  
• *country_id*: country identifier, unilateral.  
• *iso3*: ISO3 alphabetic code, unilateral.  
• *iso3num*: ISO3 numeric code, unilateral.  
• *country_exists*: 1 if country exists in a given year, unilateral.  
• *contig*: 1 if the countries are contiguous (neighbors), bilateral.  
• *distcap*: distance between the capital city of each country, in km, bilateral.  
• *dist*: distance between the most populated city of each country, in km, bilateral.  
• *distw_harmonic*: population-weighted average distance between the most populated
cities of each country, harmonic mean, in km bilateral.  
• *distw_arithmetic*: population-weighted average distance between the most populated
cities of each country, arithmetic mean, in km bilateral.  
• *distw_harmonic_jh*: weighted average distance based on satellite nightlight data, com-
puted by Julian Hinz, harmonic mean, in km bilateral.  
• *distw_arithmetic_jh*: weighted average distance based on satellite nightlight data, com-
puted by Julian Hinz, arithmetic mean, in km bilateral.  
• *main_city_source*: flag variable, indicates the source used to identify the most populated
city in the construction of dist, or to obtain the country surface used in the computation
of internal distances (both for dist and distcap), unilateral.  
• *gmt_offset_2020*: GMT offset in 2020 of the country measured in hours, unilateral.  
• *comlang_off*: 1 if countries share common official or primary language, bilateral.  
• *comlang_ethno*: 1 if countries share a common language spoken by at least 9% of the
population, bilateral.  
• *comcol*: 1 if countries share a common colonizer post 1945, bilateral.  
• *col45*: 1 if countries are or were in colonial relationship post 1945, bilateral.  
• *legal_old*: Origin of the country’s legal system. Possible values are british, french, ger-
man, scandinavian, or socialist. unilateral  
• *legal_new*: Origin of the country’s legal system, after the fall of the USSR, unilateral.
Possible values are british, french, german, scandinavian, or socialist. unilateral  
• *comleg_pretrans*: 1 if countries share common legal origins before transition, bilateral.  
• *comleg_posttrans*: 1 if countries share common legal origins after transition, bilateral.  
• *transition_legalchange*: 1 if common legal origin has changed since the fall of the USSR,
bilateral.  
• *comrelig*: Religious proximity index (Disdier and Mayer, 2007): obtained by summing
the products of the shares of Catholics, Protestants and Muslims in the origin and destina-
tion countries. Varies between 0 and 1, increases when the country pair shares a common
religion practised by a large share of the population.  
• *heg_o*: 1 if origin is current or former hegemon of destination, bilateral.  
• *heg_d*: 1 if destination is current or former hegemon of origin, bilateral.  
• *col_dep_ever*: 1 if country pair was ever in colonial relationship. Takes into account
colonial relationships before 1948, bilateral.  
• *col_dep*: 1 if country pair currently in colonial or dependency relationship, bilateral.  
• *col_dep_end_year*: Independence date from hegemon, if the pair was ever in a colonial
or dependency relationship (if col_dep_ever is equal to 1). Missing if the pair never was
in a colonial or dependency relationship (col_dep_ever= 0). Takes into account colonial
relationships before 1948, bilateral.  
• *col_dep_end_conflict*: 1 if independence involved conflict. Missing if the pair never was
in a colonial or dependency relationship (col_dep_ever= 0). Takes into account colonial
relationships before 1948, bilateral.  
• *sibling_ever*: 1 if pair ever in sibling relationship, i.e. if they ever had the same hegemon.
Takes into account colonial relationships before 1948, bilateral.  
• *sibling*: 1 if pair currently in sibling relationship, i.e. if they have the same hegemon,
bilateral.  
• *sever_year*: Severance year for sibling pairs. Corresponds to the year in which the first
sibling in the pair became independent. Takes into account colonial relationships before
1948, bilateral.  
• *empire*: Name of the hegemon if the pair is currently sibling (i.e. year is smaller than
sever_year), bilateral.  

• *sib_conflict*: 1 if pair ever in sibling relationship (sibling_ever= 1) and if their inde-
pendence from the hegemon involved a conflict with the hegemon. Takes into account
colonial relationships before 1948, bilateral.  
• *scaled_sci*: Social Connectedness Index, bilateral.  
• *diplo_disagreement*: Diplomatic disagreement, measured through UN votes, bilateral.  
• *pop*: Population, in thousands (source WDI/Maddison), unilateral.  
• *gdp*: GDP, in current thousands US$ (source WDI/Barbieri), unilateral.  
• *gdpcap*: GDP per cap, in current thousands US$ (source WDI/Barbieri), unilateral.  
• *gdp_ppp*: GDP PPP, in current thousands international $ (source WDI), unilateral.  
• *gdpcap_ppp*: GDP per cap PPP, in current thousands international $ (source WDI), uni-
lateral.  
• *pop_pwt*: Population, in thousands (source PWT), unilateral.  
• *gdp_ppp_pwt*: GDP, current PPP, in 2011 thousands US$ (source PWT), unilateral.  

• *gdp_source*: Source of GDP data: 1= WDI, 2= Barbieri, 3= Taiwan Govt, unilateral.  
• *pop_source*: Source of population data: 1= WDI, 2= Maddison, 3= Taiwan Govt,
unilateral.  
• *gatt*: 1 if the country is a GATT member, unilateral.  
• *wto*: 1 if the country is a WTO member, unilateral.  
• *eu*: 1 if country is a EU member, unilateral.  
• *fta_wto*: 1 if the country pair is engaged in a regional trade agreement, source WTO
supplemented by Thierry Mayer, bilateral.  
• *fta_wto_raw*: 1 if the country pair is engaged in a regional trade agreement, source WTO,
bilateral. 
• *rta_coverage*: Coverage of the trade agreement. 0= “no trade agreement”. 1= “goods
only”, 2= “services only”, 3= “goods and services”, bilateral.  
• *rta_type*: Type of trade agreement. PSA= “Partial Scope Agreement”, FTA= “Free Trade
Agreement”, CU= “Customs Union”, EIA= “Economic Integration Agreement”. See
below for more detailed explanations , bilateral.  
• *entry_cost*: Cost of business start-up procedures (% of GNI per capita), unilateral.  
• *entry_proc*: Number of start-up procedures to register a business, unilateral.  
• *entry_time*: Days required to start a business, unilateral.  
• *entry_tp*: Days required to start a business + number of procedures to start a business,
unilateral.  
• *tradeflow_comtrade_o*: Trade flows as reported by the origin, in 1000 current USD.
Source: Comtrade, bilateral.  
• *tradeflow_comtrade_d*: Trade flows as reported by the destination, in 1000 current USD.
Source, Comtrade, bilateral.  
• *tradeflow_baci*: Trade flow, 1000 current USD. Source: BACI, bilateral.  
• *manuf_tradeflow_baci*: Trade flow of manufactured goods, in 1000 current USD. Source:
BACI, bilateral.  
• *tradeflow_imf_o*: Trade flows as reported by the origin, in 1000 current USD. Source:
IMF, bilateral.  
• *tradeflow_imf_d*: Trade flows as reported by the destination, in 1000 current USD.
Source: IMF, bilateral.  

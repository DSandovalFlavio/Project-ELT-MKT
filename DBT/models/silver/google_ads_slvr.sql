SELECT *, 
upper( 
concat(
  replace(Company, " ", ""),"_",
  case 
    when Campaign_Type = "Email" then "EM" 
    when Campaign_Type = "Influencer" then "INF"
    when Campaign_Type = "Display" then "DSP"
    when Campaign_Type = "Search" then "SRCH"
    when Campaign_Type = "Social Media" then "SM"
    end,"_",
  replace(replace(replace(Target_Audience, "Women ", "W-"), "Men ", "M-"), "All Ages", "A-A"),"_",
  CASE
    WHEN Location = 'Nueva York' THEN 'NY'
    WHEN Location = 'Los Ángeles' THEN 'LA'
    WHEN Location = 'Chicago' THEN 'CHI'
    WHEN Location = 'San Francisco' THEN 'SF'
    WHEN Location = 'Miami' THEN 'MIA'
    WHEN Location = 'Washington D.C.' THEN 'DC'
    WHEN Location = 'Las Vegas' THEN 'LV'
    WHEN Location = 'Boston' THEN 'BOS'
    WHEN Location = 'Seattle' THEN 'SEA'
    WHEN Location = 'Nueva Orleans' THEN 'NOLA'
  END)) as Campaign_Name,
  DATE_ADD(Date, INTERVAL cast(replace(Duration, " days", "") AS INT64) DAY) as Date_End
  from {{ source("raw", "google_ads_raw")}}
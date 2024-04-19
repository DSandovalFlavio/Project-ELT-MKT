SELECT 
Date,
Campaign_Name,
source,
sum(Acquisition_Cost) as cost,
sum(Clicks) as clicks,
sum(Impressions) as impressions
FROM {{ ref("facebook_ads_slvr")}}
group by 1,2,3
union all
SELECT 
Date,
Campaign_Name,
source,
sum(Acquisition_Cost) as cost,
sum(Clicks) as clicks,
sum(Impressions) as impressions
FROM {{ ref("google_ads_slvr")}}
group by 1,2,3
union all
SELECT 
Date,
Campaign_Name,
source,
sum(Acquisition_Cost) as cost,
sum(Clicks) as clicks,
sum(Impressions) as impressions
FROM {{ ref("instagram_ads_slvr")}}
group by 1,2,3
union all
SELECT 
Date,
Campaign_Name,
source,
sum(Acquisition_Cost) as cost,
sum(Clicks) as clicks,
sum(Impressions) as impressions
FROM {{ ref("twitter_ads_slvr")}}
group by 1,2,3
union all
SELECT 
Date,
Campaign_Name,
source,
sum(Acquisition_Cost) as cost,
sum(Clicks) as clicks,
sum(Impressions) as impressions
FROM {{ ref("youtube_ads_slvr")}}
group by 1,2,3
union all
SELECT 
Date,
Campaign_Name,
source,
sum(Acquisition_Cost) as cost,
sum(Clicks) as clicks,
sum(Impressions) as impressions
FROM {{ ref("email_slvr")}}
group by 1,2,3

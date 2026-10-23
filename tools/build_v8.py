import os
S='/workspace/weekly_guide/src/'
ACC='Accessed Oct 22, 2026.'
css='''@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:Gelasio,Georgia,serif;color:#fff}
.pg{width:8.5in;height:11in;background:#001B35;position:relative;page-break-after:always;padding:.62in .6in .5in;overflow:hidden}
.pg:before{content:"";position:absolute;inset:.2in;border:1px solid #D4AF37}
.pg:after{content:"";position:absolute;inset:.26in;border:1px solid #D4AF37}
.n{position:absolute;width:.16in;height:.16in;border:1px solid #D4AF37;background:inherit;z-index:2}
.star{position:absolute;top:.08in;left:50%;transform:translateX(-50%);color:#D4AF37;font-size:22pt;background:#001B35;padding:0 6px;z-index:3;line-height:1}
h1{font-family:Cinzel;font-weight:700;text-transform:uppercase;text-align:center;font-size:30pt;margin:0;letter-spacing:1px}
h2{font-family:Cinzel;font-weight:700;color:#D4AF37;text-align:center;font-size:13pt;margin:2px 0 12px;text-transform:uppercase}
.box{border:1.5px solid #D4AF37;padding:9px 12px;margin-bottom:10px;font-size:12pt;line-height:1.35}
.box h3{font-family:Cinzel;font-weight:700;color:#D4AF37;font-size:11.5pt;margin:0 0 4px;text-transform:uppercase}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:10px}.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
.src{position:absolute;bottom:.36in;left:.5in;right:.5in;font-size:7.6pt;color:#c9c9c9;text-align:center;line-height:1.25;z-index:2}
.tag{color:#D4AF37;font-weight:700;font-size:9.5pt;border:1px solid #D4AF37;padding:0 3px;font-family:Cinzel}
.ph{border:1.5px dashed #D4AF37;background:#0a2a4a;color:#D4AF37;display:flex;align-items:center;justify-content:center;text-align:center;font-family:Cinzel;font-size:12pt;padding:10px}
table{width:100%;border-collapse:collapse;font-size:11pt}td,th{border-bottom:1px solid #3b5170;padding:3px 4px;text-align:left}th{color:#D4AF37;font-family:Cinzel;font-size:9.5pt}
.big{font-family:Cinzel;font-weight:700;font-size:26pt;color:#D4AF37}
.chart{display:flex;align-items:flex-end;justify-content:space-around;height:2.0in;border-bottom:1.5px solid #D4AF37;padding:0 10px}
.bar{width:.75in;text-align:center;font-size:10.5pt;font-weight:700}.bar div{margin-top:3px}
.lab{display:flex;justify-content:space-around;font-family:Cinzel;font-size:9pt;margin-top:4px;text-align:center}
img.ph2{width:100%;border:1.5px solid #D4AF37;object-fit:cover}
.qr{width:1.25in;height:1.25in;border:2px solid #D4AF37}
.c{text-align:center}'''
def page(body,src,star=True):
    n=''.join(f'<span class="n" style="{a}"></span>' for a in ['top:.16in;left:.16in','top:.16in;right:.16in','bottom:.16in;left:.16in','bottom:.16in;right:.16in'])
    return f'<section class="pg" style="{"" if star else "background:rgb(14,31,65)"}">{n}{"<span class=star>★</span>" if star else ""}{body}<div class="src">{src}</div></section>'
T='<span class="tag">[UNVERIFIED]</span>'
P=lambda s:f'<span class="tag">{s}</span>'
pages=[]
# 1 cover
pages.append(page(f'''<div style="height:1.0in"></div><img src="{S}a_wordmark.png" style="width:100%;display:block">
<div class="c" style="font-family:Cinzel;font-weight:700;font-size:21pt;color:#D4AF37;margin-top:14px">Week of October 23, 2026</div>
<div class="c" style="font-family:Cinzel;font-size:14pt;margin-top:6px;letter-spacing:3px">Issue No. 1 · Weekly Edition</div>
<div class="g2" style="margin-top:.55in"><img class="ph2" style="height:1.9in" src="{S}a_photo_explore.png"><img class="ph2" style="height:1.9in" src="{S}a_photo_aerial.png"></div>
<div class="c" style="margin-top:.35in;font-size:13pt;line-height:1.5">Rates · Market · Insurance &amp; Taxes · Rentals · Spencer Glen · Weekend Pick · Tools</div>
<div class="c" style="margin-top:.25in;font-family:Cinzel;font-size:12pt;color:#D4AF37">Guy Golan · eXp Realty · Call/Text 301-919-6726</div>''',
 'Wordmark and photos reused from the June 2026 Florida Gulf Coast Guide (photo origin carried over from June). DRAFT, not for publication.',star=False))
# 2 in this issue
idx=[('↗','This Week','Rates ease to 7.32%, Amendment 3 polling, quiet tropics.'),('▥','Market Update','Tampa Bay and Sarasota now buyer\'s markets; SW Florida inventory down.'),
('●','Community Focus','Spencer Glen, Pulte new builds in Riverview.'),('⛨','Insurance &amp; Taxes','Citizens rates down, condo reserves, CDD costs, Amendment 3.'),
('⌂','Rentals &amp; Relocation','HUD rents and who is really moving to Florida.'),('$','Dollars &amp; Cents','Rate buy-downs, strategy and payment math.'),
('⚑','In Development','Wellen Park Village HL approved.'),('…','Social Minute','Happy hour pick: Florence &amp; The Spice Boys, Sarasota.'),('⚙','Tools','Calculators and a call with Guy.')]
ix=''.join(f'<div style="display:flex;gap:10px;margin-bottom:9px"><div style="color:#D4AF37;font-size:17pt;width:26px">{a}</div><div><div style="font-family:Cinzel;font-weight:700;font-size:11.5pt">{b}</div><div style="font-size:11pt">{c}</div></div></div>' for a,b,c in idx)
pages.append(page(f'''<h1>In This Issue</h1><h2>Weekly Edition · Oct 23, 2026</h2>
<div style="display:grid;grid-template-columns:2.4in 1fr;gap:22px"><div><div class="box">Welcome to the first weekly Guide. Every Friday: rates, the top stories, the tropics and the local numbers that matter, in under ten minutes of reading.</div>
<img src="{S}a_headshot.png" style="width:100%;border:1.5px solid #D4AF37"><div class="box c" style="margin-top:8px"><div style="font-family:Cinzel;font-weight:700;color:#D4AF37;font-size:14pt">Guy Golan</div><div style="font-size:11pt">Local perspective you can actually use.</div></div>
<div class="c" style="font-size:11pt">Call/Text: 301-919-6726<br>guy@floridagulfcoastguide.com</div></div><div>{ix}</div></div>''',
 'Headshot reused from the June 2026 guide. Index reflects this issue. '+ACC))
# 3 this week
pages.append(page(f'''<h1>This Week</h1><h2>Rates · Top Stories · Tropics</h2>
<div class="g3"><div class="box c"><h3>30-yr fixed</h3><div class="big">7.32%</div>Freddie Mac PMMS, Oct 22. Down from 7.40%.</div>
<div class="box c"><h3>15-yr fixed</h3><div class="big">6.68%</div>Freddie Mac PMMS, Oct 22. A year ago the 30-yr was 6.19%.</div>
<div class="box c"><h3>Daily check</h3><div class="big">7.30%</div>Mortgage News Daily 30-yr, Oct 22: lowest since Sep 23.</div></div>
<div class="box"><h3>1 · Amendment 3 is polling short of 60%</h3>Early voting is underway for the Nov 3 ballot. Amendment 3 needs 60% to pass; a UNF poll shows 50% yes, 35% no. It would raise the non-school homestead exemption. It does not abolish property tax.</div>
<div class="box"><h3>2 · Tampa and Sarasota flip to buyer's markets</h3>Realtor.com's Market Clock now rates the Tampa and North Port-Bradenton-Sarasota metros as buyer's markets. In Tampa, more than 1 in 4 listings has cut its price, while rates ease to 7.32%.</div>
<div class="box"><h3>3 · Wellen Park Village HL approved</h3>North Port's commission voted 4-1 on Oct 20 to approve up to 1,875 homes on about 743 acres off South River Road. Details on the In Development page.</div>
<div class="box"><h3>Tropics &amp; weather</h3>The Gulf and Caribbean are quiet; no threat to Florida. Subtropical Storm Josephine is off New England, and a system near Bermuda has a 10% development chance. Friday: sunny, highs 80-84 from Tampa to Naples. Season ends Nov 30.</div>''',
 'Sources: Freddie Mac PMMS (freddiemac.com/pmms; FRED MORTGAGE30US); Mortgage News Daily; Florida Politics, Oct 21; WESH, Oct 14; Realtor.com via Tampa Bay Business &amp; Wealth, Oct 19; yoursun.com, Oct 22; NHC Tropical Weather Outlook 2 PM EDT Oct 22; NWS forecasts. '+ACC))
# 4 market
def bars(items,mx):
    b=''.join(f'<div class="bar" ><span>{v}</span><div style="height:{h/mx*1.6:.2f}in;background:{c}"></div></div>' for v,h,c in items)
    return f'<div class="chart">{b}</div>'
pages.append(page(f'''<h1>Market Update</h1><h2>September &amp; Q3 2026 · Buyers gain leverage</h2>
<div class="g2"><div class="box"><h3>Tampa Bay metro</h3><table><tr><td>Median list price</td><td>~$385,400 (−6.6% YoY)</td></tr><tr><td>Listings w/ price cut</td><td>27%+ (US 20.8%)</td></tr><tr><td>Median days on market</td><td>76</td></tr><tr><td>Active listings</td><td>17,965 (−3.8%)</td></tr></table></div>
<div class="box"><h3>Sarasota-Manatee (Q3)</h3><table><tr><td>Closings</td><td>5,699 (+8%)</td></tr><tr><td>SF median</td><td>Sar. $485K · Man. $490K</td></tr><tr><td>Condo median</td><td>Sar. $324,380 · Man. $307K</td></tr><tr><td>Days on mkt / price cuts</td><td>{P("Data pending (Dexter)")}</td></tr></table></div></div>
<div class="box"><h3>Sales growth, Q3 2026 vs Q3 2025 · condo vs single-family</h3>{bars([("+20.9%",20.9,"#D4AF37"),("+3.6%",3.6,"#F3E9D2"),("+26.8%",26.8,"#D4AF37"),("+3.1%",3.1,"#F3E9D2")],26.8)}
<div class="lab"><span>S-M condo/TH</span><span>S-M single-family</span><span>Sarasota condo</span><span>Florida condo</span></div></div>
<div class="g3"><div class="box"><h3>North Port / Venice</h3>The whole North Port-Bradenton-Sarasota metro is rated a buyer's market. City-level figures: {P("Data pending (Dexter)")}</div>
<div class="box"><h3>Charlotte · Lee</h3>Punta Gorda SF median $344,000 (+4.2%). Cape Coral-Fort Myers SF median $375,500 (+0.1%). Lee homes for sale 9,269 (−18.6%).</div>
<div class="box"><h3>Collier</h3>Naples SF median $785,000 (+1.6%). Active SF listings 2,297 (−13.3%); 5.5 months of supply; 108 avg. days to sale.</div></div>''',
 'Sources: Realtor.com via TBBW, Oct 19; RASM Q3 via Sarasota Magazine, Oct 22 and Herald-Tribune, Oct 20; Florida Realtors data via FGCU RERI, Oct 16; Bonnycastle Realty (Lee, Sept.); Southwest Coast Realty (Collier, Sept.; secondary source). '+ACC))
# 5 spencer glen
CAP='font-family:Cinzel;font-size:8.5pt;color:#D4AF37;letter-spacing:1px'
LB='font-family:Cinzel;font-weight:700;color:#D4AF37;font-size:10.5pt;letter-spacing:1.5px;margin-bottom:3px'
IM='position:absolute;border:1px solid #D4AF37;object-fit:cover;display:block'
HR='border-top:1px solid #D4AF37;width:1.2in;margin:9px 0'
pages.append(page(f'''<div style="font-family:Cinzel;font-size:10pt;color:#D4AF37;letter-spacing:3px;text-align:center">COMMUNITY FOCUS</div>
<h1 style="font-size:26pt">Spencer Glen</h1><h2 style="margin-bottom:0">Riverview (Tampa Bay)</h2>
<div style="position:relative;height:8.3in;margin-top:.2in">
<img src="{S}sg_hero_amenity_1600.jpg" style="{IM};left:0;top:0;width:4.3in;height:2.55in">
<div style="position:absolute;left:0;top:2.6in;{CAP}">The amenity center · resort pool and clubhouse</div>
<div style="position:absolute;left:4.6in;top:0;width:2.7in;font-size:11pt;line-height:1.45"><div style="{LB}">THE BUZZ</div><span style="float:left;font-family:Cinzel;font-weight:700;color:#D4AF37;font-size:36pt;line-height:.85;margin:4px 6px 0 0">A</span> new-construction Pulte Homes single-family community in Riverview, Hillsborough County, about a mile from the I-75/Big Bend interchange and US 301. Sales office: 13716 Sunlight Meadow Dr.</div>
<img src="{S}sg_clubhouse_1100.jpg" style="{IM};left:4.0in;top:2.4in;width:3.3in;height:3.0in;z-index:2;box-shadow:0 0 0 6px #001B35">
<div style="position:absolute;right:0;top:5.47in;{CAP}">The clubhouse</div>
<div style="position:absolute;left:0;top:3.05in;width:3.65in;font-size:11pt;line-height:1.45"><div style="{LB}">THE HOMES</div>1,662 to 4,272 sq ft, 3-5 bedrooms. Builder base prices from $400,990 (Crestmere) to $712,990+ (Roseland). Base prices change often.
<div style="{HR}"></div><div style="{LB}">AMENITIES</div>Clubhouse, zero-entry pool with cabanas, fitness center, pickleball, dog park and trails. Pulte lists a 10-year structural and 5-year leak warranty.</div>
<img src="{S}sg_streets_1600.jpg" style="{IM};left:0;top:5.85in;width:3.9in;height:1.48in">
<div style="position:absolute;left:0;top:7.4in;{CAP}">Streets and homes · aerial</div>
<div style="position:absolute;left:4.2in;top:5.85in;width:3.1in;font-size:11pt;line-height:1.45"><div style="{LB}">ALSO HERE</div>Kinward at Spencer Glen is a separate build-to-rent townhome community with 3-4 bedroom rentals. CDD and HOA fees: {P("Pending: ask Pulte")}
<div style="{HR}"></div><div style="{LB}">GUY'S TAKE</div>{P("[Guy to write]")}</div>
</div>''',
 'Sources: pulte.com (Spencer Glen); Redfin and Realtor.com listings; kinwardatspencerglen.com. Prices are builder base prices and subject to change. Photos: Guy Golan. '+ACC))
# 6 insurance & taxes
pages.append(page(f'''<h1>Insurance &amp; Taxes</h1><h2>What changes the real cost of owning</h2>
<div class="g2"><div class="box"><h3>Citizens</h3>Homeowners multiperil rates are down an average 8.8% in 2026; wind-only about 5%. Policies fell to 266,093 (Aug 28) from a 1.41M peak. Citizens resumed writing policies Oct 10.</div>
<div class="box"><h3>Condo Associations</h3>Citizens condo association rates are still rising: about +7.7% multiperil and +14.1% wind-only. Hurricane Isaias hit the Panhandle; AM Best calls it an "earnings event," not a pricing surge.</div>
<div class="box"><h3>Flood Zone Note</h3>Homeowners policies generally don't cover flood. Check the property's flood zone and get a flood quote before you write an offer, even outside required zones.</div>
<div class="box"><h3>Amendment 3 · Nov 3</h3>Raises the non-school homestead exemption to $150K in 2027 and $250K in 2028, then indexes it to inflation. It does not abolish property tax. Needs 60%. Supporters cite savings; opponents cite local budget cuts.</div>
<div class="box"><h3>Condo Reserves</h3>Since Oct 4, DBPR rule 61B-22.005 requires associations to fund reserves according to their latest structural integrity reserve study (SIRS). A clarifying amendment was proposed Oct 22.</div>
<div class="box"><h3>CDD Costs</h3>One Parrish lot type (Wildleaf 45', North River Ranch) went from $2,351 in FY2024 to $2,882 in FY2027, about +23%. Check the district's adopted schedule, not the brochure.</div></div>''',
 'Sources: Citizens Property Insurance (citizensfla.com); C&amp;S blog, Oct 2; Insurance Journal, Oct 19; WESH, Oct 14; Florida Politics, Oct 21; DBPR rule 61B-22.005 (flrules.org); Roetzel &amp; Andress, Oct 19; North River Ranch ISD adopted assessments (verified Oct 18). Flood note is general guidance. '+ACC))
# 7 rentals
pages.append(page(f'''<h1>Rentals &amp; Relocation</h1><h2>Rents are flat · Who is moving here</h2>
<div class="box"><h3>HUD FY2026 Fair Market Rents</h3><table><tr><th>Metro</th><th>Studio</th><th>1BR</th><th>2BR</th><th>3BR</th></tr>
<tr><td>North Port-Bradenton-Sarasota</td><td>$1,418</td><td>$1,686</td><td>$1,958</td><td>$2,537</td></tr><tr><td>Tampa-St. Pete</td><td>$1,593</td><td>$1,696</td><td>$1,977</td><td>$2,527</td></tr><tr><td>Punta Gorda</td><td>$1,159</td><td>$1,167</td><td>$1,470</td><td>$2,041</td></tr></table>
<div style="font-size:10pt;margin-top:4px">Lee and Collier: {P("Data pending (Dexter)")}</div></div>
<div class="g2"><div class="box"><h3>Tampa Market Rents</h3>Zillow typical rent $1,991 (+0.4%, Sept.). Realtor.com median asking rent, studio-2BR, $1,608 (−3.1%), and 62.4% of listings offer concessions.</div>
<div class="box"><h3>Takeaway</h3>Tampa rents are flat to down, and most landlords are offering deals. Renters can negotiate; investors should underwrite conservatively.</div></div>
<div class="box"><h3>Census migration · July 2024-July 2025 (two separate measures)</h3>
{bars([("201,191",201191,"#D4AF37"),("178,674",178674,"#F3E9D2"),("22,517",22517,"#D4AF37")],201191)}
<div class="lab"><span>Total net migration</span><span>Net international</span><span>Net domestic</span></div>
<div style="font-size:11pt;margin-top:6px">Total is down from 598,737 in 2022. Hillsborough and Pinellas had net domestic outflow.</div></div>''',
 'Sources: HUD FY2026 Fair Market Rents (huduser.gov, verified Oct 22); Zillow Sept. 2026 rent report; Realtor.com Sept. 2026 rental report; U.S. Census Vintage 2025 via UF News, Jul 13, 2026. '+ACC))
# 8 dollars
mx=2748
pages.append(page(f'''<h1>Dollars &amp; Cents</h1><h2>Payment strategy still matters</h2>
<div class="g2"><div class="box"><h3>Rates We Saw</h3>Freddie Mac PMMS (Oct 22): 30-year fixed 7.32%, 15-year 6.68%. Mortgage News Daily's daily index hit 7.30%. PMMS is a weekly average; MND is a daily top-tier rate.</div>
<div class="box"><h3>Incentives Worth Noting</h3>Rate buy-downs, closing-cost help and builder incentives. Ask what each one costs, whether it is temporary, and what the payment is after it ends.</div>
<div class="box"><h3>Buying Strategy</h3>With more than 1 in 4 Tampa listings cutting price, buyers can negotiate price, credits and timing. Compare APR, points and closing costs, not just the rate.</div>
<div class="box"><h3>Selling Strategy</h3>Price right from day one. Homes in Tampa sit about 76 days; a well-presented, well-priced listing avoids chasing the market down.</div></div>
<div class="box"><h3>Example monthly payment · $400,000 loan · principal &amp; interest only</h3>
{bars([("$2,748",2748,"#F3E9D2"),("$2,742",2742,"#D4AF37"),("$3,524",3524,"#D4AF37")],3524)}
<div class="lab"><span>30-yr @ 7.32%<br>PMMS</span><span>30-yr @ 7.30%<br>MND</span><span>15-yr @ 6.68%<br>PMMS</span></div>
<div class="c" style="font-family:Cinzel;color:#D4AF37;font-size:10pt;margin-top:6px">Illustrative only · NOT A RATE QUOTE</div></div>''',
 'Sources: Freddie Mac PMMS, Oct 22, 2026; Mortgage News Daily, Oct 22, 2026. Payments are illustrative principal and interest calculations; they exclude taxes, insurance, HOA/CDD and PMI. Not a rate quote or loan offer. '+ACC))
# 9 in development
pages.append(page(f'''<h1>In Development</h1><h2>North Port · Wellen Park keeps growing</h2>
<div class="g2"><div class="box c"><h3>Village HL</h3><div class="big">1,875</div>homes, maximum</div><div class="box c"><h3>Wellen Park buildout</h3><div class="big">22,000</div>homes (developer figure)</div></div>
<div class="box"><h3>What Was Approved</h3>On Oct 20, North Port's City Commission voted 4-1 to approve the Village HL master concept plan: up to 1,875 homes on about 743 acres off South River Road near the Myakka River, plus 400,000 sq ft of retail and 100,000 sq ft of medical and office space. Residents raised environmental concerns.</div>
<div class="box"><h3>Winchester Ranch: Not Approved</h3>On Oct 10 the commission voted 3-2 only to be willing to hear an application for Winchester Ranch (about 3,000 acres, around 6,500 homes, two hospital campuses). Nothing has been approved.</div>
<div class="box"><h3>Why It Matters</h3>More new-construction supply in a metro already rated a buyer's market. Buyers get choices; resale sellers compete with builders.</div>''',
 'Sources: yoursun.com, Oct 22 and Oct 10; DocketCity, North Port Res. No. 2026-R-68 (passed Oct 20). '+ACC))
# 10 social
CAP='font-family:Cinzel;font-size:8.5pt;color:#D4AF37;letter-spacing:1px'
LB='font-family:Cinzel;font-weight:700;color:#D4AF37;font-size:10.5pt;letter-spacing:1.5px;margin-bottom:3px'
PH='position:absolute;border:1px solid #D4AF37;background:#0a2a4a;color:#D4AF37;display:flex;align-items:center;justify-content:center;text-align:center;font-family:Cinzel;font-size:11pt;padding:10px'
HR='border-top:1px solid #D4AF37;width:1.2in;margin:8px 0'
pages.append(page(f'''<div style="font-family:Cinzel;font-size:10pt;color:#D4AF37;letter-spacing:3px;text-align:center">SOCIAL MINUTE</div>
<h1 style="font-size:24pt">Happy Hour Pick</h1><h2 style="margin-bottom:4px">Florence &amp; The Spice Boys</h2>
<div class="c" style="font-style:italic;color:#e9dcb0;font-size:12pt">Israeli &amp; Middle Eastern fusion, Sarasota</div>
<div style="position:relative;height:8.2in;margin-top:.22in">
<div style="position:absolute;left:0;top:.05in;width:3.05in"><div style="font-size:12pt;line-height:1.5"><span style="float:left;font-family:Cinzel;font-weight:700;color:#D4AF37;font-size:40pt;line-height:.85;margin:4px 6px 0 0">A</span> colorful Middle Eastern fusion spot that started as the Spice Boys food truck in 2019. Partner chef Collin Blakeman trained under Thomas Keller at The French Laundry. Go early, grab a seat, and order the Jerusalem beef pita (arayes) with amba cream.</div>
<div style="border-top:1px solid #D4AF37;border-bottom:1px solid #D4AF37;margin-top:14px;padding:8px 2px;font-family:Cinzel;font-weight:700;color:#D4AF37;font-size:11.5pt;text-align:center;line-height:1.35">"Order the Jerusalem beef pita."</div></div>
<div style="{PH};right:0;top:0;width:3.95in;height:3.35in">PHOTO: Dish — Guy's own photo pending</div>
<div style="position:absolute;right:0;top:3.42in;{CAP}">The dish · Jerusalem beef pita</div>
<div style="{PH};left:0;top:3.05in;width:3.55in;height:2.45in;z-index:2;box-shadow:0 0 0 6px #001B35">PHOTO: Cocktail — real photo pending</div>
<div style="position:absolute;left:0;top:5.6in;{CAP}">At the bar · happy hour</div>
<div style="position:absolute;left:3.9in;top:3.62in;width:3.4in;font-size:11pt;line-height:1.45">
<div style="{LB}">HAPPY HOUR · UTC</div>257 N Cattlemen Rd, Unit 90, Sarasota · <span style="white-space:nowrap">(941) 359-8338</span><br><b>Daily 3-5 PM</b> {P("CONFIRM BEFORE PRINT")}<br>$6 margarita · $7 martini of the day<br>$5 draft, prosecco, Cabernet or Sauvignon Blanc<br>$5 bites: hummus, pitas, tempura cauliflower
<div style="{HR}"></div><div style="{LB}">BONUS HOUR</div>99¢ martini daily 5-6 PM with a regular menu item {P("CONFIRM BEFORE PRINT")}</div>
<div style="position:absolute;left:0;top:6.72in;width:2.75in;font-size:11.5pt;line-height:1.45"><div style="{LB}">ALSO · THE LANDINGS</div>4990 S Tamiami Trail, Sarasota · Happy hour Monday to Saturday, <span style="white-space:nowrap">3-5 PM</span></div>
<div style="{PH};right:0;top:6.68in;width:4.2in;height:1.0in">PHOTO: Restaurant — real photo pending</div>
<div style="position:absolute;right:0;top:7.75in;{CAP}">The room · West District at UTC</div>
<div style="position:absolute;left:0;right:0;top:8.02in;text-align:center;font-size:9.5pt;color:#D4AF37;font-style:italic">Local suggestion, not a sponsorship.</div>
</div>''',
 'Sources: florenceandthespiceboys.com (UTC and Landings happy hour menus, About page); utcsarasota.com listing; Your Observer, May 20, 2026; Bradenton Herald, 2025. '+ACC))
# 11 tools
tool=lambda t,d,u,q:f'<div class="box" style="display:flex;gap:14px;align-items:center">{q}<div><h3>{t}</h3>{d}<div style="font-size:9.5pt;color:#D4AF37;margin-top:3px">{u}</div></div></div>'
pend='<div class="qr ph" style="font-size:9pt">QR pending URL</div>'
pages.append(page(f'''<h1>Tools</h1><h2>Run the numbers · Then talk to Guy</h2>
{tool("Mortgage Calculator","Estimate your monthly payment with taxes, insurance and HOA.",P("[URL pending]"),pend)}
{tool("Cost-of-Moving Estimator","See what a move to the Gulf Coast really costs before you pack.","guyfgolan.github.io/relocation-cost-estimator",f'<img class="qr" src="{S}qr_moving.png">')}
{tool("Area Matcher · Discover Sarasota-Tampa Bay","Answer a few questions and find the areas that fit how you live.",P("[URL pending]"),pend)}
{tool("Buying or selling? Scan to schedule a call","Book a time with Guy Golan. Call/Text 301-919-6726 · guy@floridagulfcoastguide.com","calendar.app.google/8GQcVfui78JUZLCP7",f'<img class="qr" src="{S}qr_call.png">')}''',
 'Tools are for estimates only and are not financial advice. Guy Golan, eXp Realty. DRAFT, not for publication. '+ACC))
html=f'<html><head><meta charset=utf-8><style>{css}</style></head><body>{"".join(pages)}</body></html>'
open('/workspace/weekly_guide/weekly_guide_2026-10-23_v8.html','w').write(html)

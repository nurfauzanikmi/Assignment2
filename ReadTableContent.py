Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib2
>>> request = urllib2.Request("http://fskm.uitm.edu.my/v1/fakulti/staff-directory/academic/1097.html")
>>> handle = urllib2.urlopen(request)
content = handle.read()
>>> splitted_page = content.split("<ul>", 1);

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    splitted_page = content.split("<ul>", 1);
NameError: name 'content' is not defined
>>> content = handle.read()
>>> splitted_page = content.split("<ul>", 1);
>>> splitted_page = splitted_page[0].split("</ul>", 1)
>>> print "Content: "+splitted_page[1]
Content: </div></div>
</div></div></li><li class="mega last"><a href="/v1/home/news.html" class="mega last" id="menu161" title="News"><span class="menu-title">News</span></a></li></ul></div></div>
</div></div></li><li class="mega active haschild"><a href="#" class="mega active haschild" id="menu194" title="Faculty"><span class="menu-title">Faculty</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level1"><li class="mega first haschild"><a href="#" class="mega first haschild" id="menu54" title="About Faculty"><span class="menu-title">About Faculty</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level2"><li class="mega first"><a href="/v1/fakulti/about-faculty/deans-message.html" class="mega first" id="menu55" title="Dean's Message"><span class="menu-title">Dean's Message</span></a></li><li class="mega"><a href="/v1/fakulti/about-faculty/deputy-dean.html" class="mega" id="menu99" title="Deputy Dean"><span class="menu-title">Deputy Dean</span></a></li><li class="mega"><a href="/v1/fakulti/about-faculty/organization-chart.html" class="mega" id="menu100" title="Organization Chart"><span class="menu-title">Organization Chart</span></a></li><li class="mega"><a href="/v1/fakulti/about-faculty/vision-mission-a-objective.html" class="mega" id="menu65" title="Vision, Mission &amp; Objective"><span class="menu-title">Vision, Mission &amp; Objective</span></a></li><li class="mega"><a href="/v1/fakulti/about-faculty/history.html" class="mega" id="menu66" title="History"><span class="menu-title">History</span></a></li><li class="mega last"><a href="/v1/fakulti/about-faculty/location-map.html" class="mega last" id="menu68" title="Location Map"><span class="menu-title">Location Map</span></a></li></ul></div></div>
</div></div></li><li class="mega active haschild"><a href="#" class="mega active haschild" id="menu56" title="Staff Directory"><span class="menu-title">Staff Directory</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level2"><li class="mega active first"><a href="/v1/fakulti/staff-directory/academic.html" class="mega active first" id="menu60" title="Academic"><span class="menu-title">Academic</span></a></li><li class="mega last"><a href="/v1/fakulti/staff-directory/non-academic.html" class="mega last" id="menu61" title="Non Academic"><span class="menu-title">Non Academic</span></a></li></ul></div></div>
</div></div></li><li class="mega last"><a href="/v1/fakulti/quality--fskm.html" class="mega last" id="menu193" title="Quality @ FSKM"><span class="menu-title">Quality @ FSKM</span></a></li></ul></div></div>
</div></div></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu58" title="Academic"><span class="menu-title">Academic</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level1"><li class="mega first haschild"><a href="#" class="mega first haschild" id="menu70" title="Postgraduate"><span class="menu-title">Postgraduate</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level2"><li class="mega first haschild"><a href="#" class="mega first haschild" id="menu187" title="Phd"><span class="menu-title">Phd</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 350px;"><div class="megacol column1 first" style="width: 350px;"><ul class="megamenu level3"><li class="mega first"><a href="/v1/academic/postgraduate/phd/doctor-of-philosophy-computer-science-cs950.html" class="mega first" id="menu174" title="Doctor of Philosophy (Computer Science) - CS950"><span class="menu-title">Doctor of Philosophy (Computer Science) - CS950</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/phd/doctor-of-philosophy-information-technology-cs951.html" class="mega" id="menu175" title="Doctor of Philosophy (Information Technology) - CS951"><span class="menu-title">Doctor of Philosophy (Information Technology) - CS951</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/phd/doctor-of-philosophy-mathematics-cs952.html" class="mega" id="menu176" title="Doctor of Philosophy (Mathematics) -CS952"><span class="menu-title">Doctor of Philosophy (Mathematics) -CS952</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/phd/doctor-of-philosophy-statistics-cs953.html" class="mega" id="menu177" title="Doctor of Philosophy (Statistics) - CS953"><span class="menu-title">Doctor of Philosophy (Statistics) - CS953</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/phd/doctor-of-philosophy-decision-science-cs954.html" class="mega" id="menu178" title="Doctor of Philosophy (Decision Science) - CS954"><span class="menu-title">Doctor of Philosophy (Decision Science) - CS954</span></a></li><li class="mega last"><a href="/v1/academic/postgraduate/phd/doctor-of-philosophy-actuarial-science-cs955.html" class="mega last" id="menu179" title="Doctor of Philosophy (Actuarial Science) - CS955"><span class="menu-title">Doctor of Philosophy (Actuarial Science) - CS955</span></a></li></ul></div></div>
</div></div></li><li class="mega last haschild"><a href="#" class="mega last haschild" id="menu188" title="Master"><span class="menu-title">Master</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 350px;"><div class="megacol column1 first" style="width: 350px;"><ul class="megamenu level3"><li class="mega first"><a href="/v1/academic/postgraduate/master/master-of-science-in-applied-statistics-cs702.html" class="mega first" id="menu74" title="Master of Science in Applied Statistics - CS702"><span class="menu-title">Master of Science in Applied Statistics - CS702</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-computer-science-cs707.html" class="mega" id="menu180" title="Master of Computer Science - CS707"><span class="menu-title">Master of Computer Science - CS707</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-science-in-computer-networking-cs708.html" class="mega" id="menu77" title="Master of Science in Computer Networking - CS708"><span class="menu-title">Master of Science in Computer Networking - CS708</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-science-computer-science-cs750.html" class="mega" id="menu76" title="Master of Science (Computer Science) - CS750"><span class="menu-title">Master of Science (Computer Science) - CS750</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-science-information-technology-cs751.html" class="mega" id="menu181" title="Master of Science (Information Technology) - CS751"><span class="menu-title">Master of Science (Information Technology) - CS751</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-science-mathematics-cs752.html" class="mega" id="menu182" title="Master of Science (Mathematics) - CS752"><span class="menu-title">Master of Science (Mathematics) - CS752</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-science-statistics-cs753.html" class="mega" id="menu183" title="Master of Science (Statistics) - CS753"><span class="menu-title">Master of Science (Statistics) - CS753</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-science-decision-science-cs754.html" class="mega" id="menu184" title="Master of Science (Decision Science) - CS754"><span class="menu-title">Master of Science (Decision Science) - CS754</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-science-actuarial-science-cs755.html" class="mega" id="menu185" title="Master of Science (Actuarial Science) - CS755"><span class="menu-title">Master of Science (Actuarial Science) - CS755</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-science-in-information-technology-cs770.html" class="mega" id="menu73" title="Master of Science in Information Technology - CS770"><span class="menu-title">Master of Science in Information Technology - CS770</span></a></li><li class="mega"><a href="/v1/academic/postgraduate/master/master-of-quantitative-sciences-cs771.html" class="mega" id="menu71" title="Master of Quantitative Sciences - CS771"><span class="menu-title">Master of Quantitative Sciences - CS771</span></a></li><li class="mega last"><a href="/v1/academic/postgraduate/master/master-of-science-in-applied-mathematics-cs773.html" class="mega last" id="menu186" title="Master of Science in Applied Mathematics - CS773"><span class="menu-title">Master of Science in Applied Mathematics - CS773</span></a></li></ul></div></div>
</div></div></li></ul></div></div>
</div></div></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu72" title="Undergraduate"><span class="menu-title">Undergraduate</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level2"><li class="mega first haschild"><a href="#" class="mega first haschild" id="menu124" title="Bachelor"><span class="menu-title">Bachelor</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 520px;"><div class="megacol column1 first" style="width: 520px;"><ul class="megamenu level3"><li class="mega first"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-computer-science-hons-cs230.html" class="mega first" id="menu86" title="Bachelor of Computer Science (Hons) - CS230"><span class="menu-title">Bachelor of Computer Science (Hons) - CS230</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-information-technology-hons-cs240.html" class="mega" id="menu96" title="Bachelor of Information Technology (Hons) - CS240"><span class="menu-title">Bachelor of Information Technology (Hons) - CS240</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-science-hons-statistics-cs241.html" class="mega" id="menu95" title="Bachelor of Science (Hons) Statistics - CS241"><span class="menu-title">Bachelor of Science (Hons) Statistics - CS241</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-science-hons-actuarial-science-cs222.html" class="mega" id="menu94" title="Bachelor of Science (Hons) Actuarial Science - CS242"><span class="menu-title">Bachelor of Science (Hons) Actuarial Science - CS242</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-information-technology-hons-intelligent-system-engineering-cs243.html" class="mega" id="menu93" title="Bachelor of Information Technology (Hons) Intelligent System Engineering - CS243"><span class="menu-title">Bachelor of Information Technology (Hons) Intelligent System Engineering - CS243</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-information-technology-hons-business-computing-cs244.html" class="mega" id="menu92" title="Bachelor of Information Technology (Hons) Business Computing - CS244"><span class="menu-title">Bachelor of Information Technology (Hons) Business Computing - CS244</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-computer-science-hons-data-communication-a-networking-cs245.html" class="mega" id="menu91" title="Bachelor of Computer Science (Hons) Data Communication &amp; Networking - CS245"><span class="menu-title">Bachelor of Computer Science (Hons) Data Communication &amp; Networking - CS245</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-information-technology-hons-information-system-engineering-cs246.html" class="mega" id="menu90" title="Bachelor of Information Technology (Hons) Information System Engineering - CS246"><span class="menu-title">Bachelor of Information Technology (Hons) Information System Engineering - CS246</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-science-hons-computational-mathematics-cs247.html" class="mega" id="menu89" title="Bachelor of Science (Hons) Computational Mathematics - CS247"><span class="menu-title">Bachelor of Science (Hons) Computational Mathematics - CS247</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-science-hons-management-mathematics-cs248.html" class="mega" id="menu88" title="Bachelor of Science (Hons) Management Mathematics - CS248"><span class="menu-title">Bachelor of Science (Hons) Management Mathematics - CS248</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-science-hons-mathematics-cs229.html" class="mega" id="menu87" title="Bachelor of Science (Hons) Mathematics - CS249"><span class="menu-title">Bachelor of Science (Hons) Mathematics - CS249</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-computer-science-hons-netcentric-computing-cs251.html" class="mega" id="menu85" title="Bachelor of Computer Science (Hons) Netcentric Computing - CS251"><span class="menu-title">Bachelor of Computer Science (Hons) Netcentric Computing - CS251</span></a></li><li class="mega last"><a href="/v1/academic/undergraduate/bachelor/bachelor-of-computer-science-hons-multimedia-computing-cs253.html" class="mega last" id="menu84" title="Bachelor of Computer Science (Hons) Multimedia Computing - CS253"><span class="menu-title">Bachelor of Computer Science (Hons) Multimedia Computing - CS253</span></a></li></ul></div></div>
</div></div></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu125" title="Diploma"><span class="menu-title">Diploma</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 290px;"><div class="megacol column1 first" style="width: 290px;"><ul class="megamenu level3"><li class="mega first"><a href="/v1/academic/undergraduate/diploma/diploma-in-computer-science-cs110.html" class="mega first" id="menu83" title="Diploma in Computer Science - CS110"><span class="menu-title">Diploma in Computer Science - CS110</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/diploma/diploma-in-statistics-cs111.html" class="mega" id="menu82" title="Diploma in Statistics - CS111"><span class="menu-title">Diploma in Statistics - CS111</span></a></li><li class="mega"><a href="/v1/academic/undergraduate/diploma/diploma-in-actuarial-science-cs112.html" class="mega" id="menu81" title="Diploma in Actuarial Science - CS112"><span class="menu-title">Diploma in Actuarial Science - CS112</span></a></li><li class="mega last"><a href="/v1/academic/undergraduate/diploma/diploma-in-mathematical-sciences-cs143.html" class="mega last" id="menu80" title="Diploma in Mathematical Sciences - CS143"><span class="menu-title">Diploma in Mathematical Sciences - CS143</span></a></li></ul></div></div>
</div></div></li><li class="mega last"><a href="/v1/academic/undergraduate/pengajian-luar-kampus-plk.html" class="mega last" id="menu218" title="Pengajian Luar Kampus (PLK)"><span class="menu-title">Pengajian Luar Kampus (PLK)</span></a></li></ul></div></div>
</div></div></li><li class="mega"><a href="http://hea.uitm.edu.my" target="_blank" class="mega" id="menu164" title="Academic Affairs Division"><span class="menu-title">Academic Affairs Division</span></a></li><li class="mega"><a href="/v1/academic/calendars.html" class="mega" id="menu162" title="Calendars"><span class="menu-title">Calendars</span></a></li><li class="mega"><a href="/v1/academic/downloads.html" class="mega" id="menu160" title="Downloads"><span class="menu-title">Downloads</span></a></li><li class="mega"><a href="http://quickr.uitm.edu.my/LotusQuickr/bhea/Main.nsf?Login&amp;RedirectTo=%2FLotusQuickr%2Fbhea%2FMain.nsf%2Fh_Toc%2F80B5E629AE3D9039482579C0002A0571%2F%3FOpenDocument" target="_blank" class="mega" id="menu195" title="Academic Affairs Circular"><span class="menu-title">Academic Affairs Circular</span></a></li><li class="mega last haschild"><a href="#" class="mega last haschild" id="menu197" title="PEO / PLO"><span class="menu-title">PEO / PLO</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level2"><li class="mega first haschild"><a href="#" class="mega first haschild" id="menu198" title="Diploma"><span class="menu-title">Diploma</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level3"><li class="mega first"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs110.pdf" target="_blank" class="mega first" id="menu200" title="CS110"><span class="menu-title">CS110</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs111.pdf" target="_blank" class="mega" id="menu201" title="CS111"><span class="menu-title">CS111</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs112.pdf" target="_blank" class="mega" id="menu202" title="CS112"><span class="menu-title">CS112</span></a></li><li class="mega last"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs143.pdf" target="_blank" class="mega last" id="menu203" title="CS143"><span class="menu-title">CS143</span></a></li></ul></div></div>
</div></div></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu199" title="Bachelor"><span class="menu-title">Bachelor</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level3"><li class="mega first"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs230.pdf" target="_blank" class="mega first" id="menu204" title="CS230"><span class="menu-title">CS230</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs240.pdf" target="_blank" class="mega" id="menu205" title="CS240"><span class="menu-title">CS240</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs241.pdf" target="_blank" class="mega" id="menu206" title="CS241"><span class="menu-title">CS241</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs242.pdf" target="_blank" class="mega" id="menu207" title="CS242"><span class="menu-title">CS242</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs243.pdf" target="_blank" class="mega" id="menu208" title="CS243"><span class="menu-title">CS243</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs244.pdf" target="_blank" class="mega" id="menu209" title="CS244"><span class="menu-title">CS244</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs245.pdf" target="_blank" class="mega" id="menu210" title="CS245"><span class="menu-title">CS245</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs246.pdf" target="_blank" class="mega" id="menu211" title="CS246"><span class="menu-title">CS246</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs247.pdf" target="_blank" class="mega" id="menu212" title="CS247"><span class="menu-title">CS247</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs248.pdf" target="_blank" class="mega" id="menu213" title="CS248"><span class="menu-title">CS248</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs249.pdf" target="_blank" class="mega" id="menu214" title="CS249"><span class="menu-title">CS249</span></a></li><li class="mega"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs251.pdf" target="_blank" class="mega" id="menu215" title="CS251"><span class="menu-title">CS251</span></a></li><li class="mega last"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs253.pdf" target="_blank" class="mega last" id="menu216" title="CS253"><span class="menu-title">CS253</span></a></li></ul></div></div>
</div></div></li><li class="mega last haschild"><a href="#" class="mega last haschild" id="menu236" title="Postgraduate"><span class="menu-title">Postgraduate</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level3"><li class="mega first"><a href="/v1/images/stories/dokumen/peoplo/peo%20plo%20cs770.pdf" class="mega first" id="menu235" title="CS770"><span class="menu-title">CS770</span></a></li></ul></div></div>
</div></div></li></ul></div></div>
</div></div></li></ul></div></div>
</div></div></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu62" title="Centre of Studies"><span class="menu-title">Centre of Studies</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 310px;"><div class="megacol column1 first" style="width: 310px;"><ul class="megamenu level1"><li class="mega first"><a href="/v1/centre-of-studies/head-centre-of-studies.html" class="mega first" id="menu97" title="Head Centre of Studies"><span class="menu-title">Head Centre of Studies</span></a></li><li class="mega"><a href="/v1/centre-of-studies/computer-science-studies.html" class="mega" id="menu103" title="Computer Science Studies"><span class="menu-title">Computer Science Studies</span></a></li><li class="mega"><a href="/v1/centre-of-studies/information-system-studies.html" class="mega" id="menu102" title="Information System Studies"><span class="menu-title">Information System Studies</span></a></li><li class="mega"><a href="/v1/centre-of-studies/information-technology-studies.html" class="mega" id="menu104" title="Information Technology Studies"><span class="menu-title">Information Technology Studies</span></a></li><li class="mega"><a href="/v1/centre-of-studies/computer-technology-a-networking-studies.html" class="mega" id="menu138" title="Computer Technology &amp; Networking Studies"><span class="menu-title">Computer Technology &amp; Networking Studies</span></a></li><li class="mega"><a href="/v1/centre-of-studies/actuarial-science-studies.html" class="mega" id="menu106" title="Actuarial Science Studies"><span class="menu-title">Actuarial Science Studies</span></a></li><li class="mega"><a href="/v1/centre-of-studies/mathematical-sciences-studies.html" class="mega" id="menu107" title="Mathematical  Sciences Studies"><span class="menu-title">Mathematical  Sciences Studies</span></a></li><li class="mega last"><a href="/v1/centre-of-studies/statistical-a-decision-science-studies.html" class="mega last" id="menu105" title="Statistical &amp; Decision Science Studies"><span class="menu-title">Statistical &amp; Decision Science Studies</span></a></li></ul></div></div>
</div></div></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu63" title="Research &amp; Development"><span class="menu-title">Research &amp; Development</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 280px;"><div class="megacol column1 first" style="width: 280px;"><ul class="megamenu level1"><li class="mega first haschild"><a href="#" class="mega first haschild" id="menu108" title="Research Theme/Group (RIG)"><span class="menu-title">Research Theme/Group (RIG)</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 240px;"><div class="megacol column1 first" style="width: 240px;"><ul class="megamenu level2"><li class="mega first"><a href="/v1/research-a-development/research-themegroup-rig/computer-science.html" class="mega first" id="menu139" title="Computer Science"><span class="menu-title">Computer Science</span></a></li><li class="mega"><a href="/v1/research-a-development/research-themegroup-rig/information-system.html" class="mega" id="menu140" title="Information System"><span class="menu-title">Information System</span></a></li><li class="mega"><a href="/v1/research-a-development/research-themegroup-rig/information-technology.html" class="mega" id="menu141" title="Information Technology"><span class="menu-title">Information Technology</span></a></li><li class="mega"><a href="/v1/research-a-development/research-themegroup-rig/computer-technology-a-networking.html" class="mega" id="menu142" title="Computer Technology &amp; Networking"><span class="menu-title">Computer Technology &amp; Networking</span></a></li><li class="mega"><a href="/v1/research-a-development/research-themegroup-rig/actuarial-science.html" class="mega" id="menu144" title="Actuarial Science"><span class="menu-title">Actuarial Science</span></a></li><li class="mega"><a href="/v1/research-a-development/research-themegroup-rig/mathematical-science.html" class="mega" id="menu143" title="Mathematical Science"><span class="menu-title">Mathematical Science</span></a></li><li class="mega last"><a href="/v1/research-a-development/research-themegroup-rig/statistical-a-decision-science.html" class="mega last" id="menu145" title="Statistical &amp; Decision Science"><span class="menu-title">Statistical &amp; Decision Science</span></a></li></ul></div></div>
</div></div></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu110" title="Journal &amp; Publications"><span class="menu-title">Journal &amp; Publications</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 430px;"><div class="megacol column1 first" style="width: 430px;"><ul class="megamenu level2"><li class="mega first"><a href="http://prisma.uitm.edu.my/PRISMa09/electronicDirectory.php?Name=&amp;Department=FAKULTI+SAINS+KOMPUTER+%26+MATEMATIK%28FSKM%29&amp;Submit=Submit" class="mega first" id="menu111" title="FSKM Staff Publications"><span class="menu-title">FSKM Staff Publications</span></a></li><li class="mega"><a href="http://rmi.uitm.edu.my/prisma.html" target="_blank" class="mega" id="menu136" title="Publication Repository Information System Management (PRISMa)"><span class="menu-title">Publication Repository Information System Management (PRISMa)</span></a></li><li class="mega last"><a href="http://ires.uitm.edu.my/ires/" class="mega last" id="menu137" title="RMI Reporting System (iReS)"><span class="menu-title">RMI Reporting System (iReS)</span></a></li></ul></div></div>
</div></div></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu114" title="Internal / External Funding"><span class="menu-title">Internal / External Funding</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 200px;"><div class="megacol column1 first" style="width: 200px;"><ul class="megamenu level2"><li class="mega first"><a href="/v1/research-a-development/internal--external-funding/2013-funding.html" class="mega first" id="menu134" title="2013 Funding"><span class="menu-title">2013 Funding</span></a></li><li class="mega"><a href="/v1/research-a-development/internal--external-funding/2012-funding.html" class="mega" id="menu135" title="2012 Funding"><span class="menu-title">2012 Funding</span></a></li><li class="mega"><a href="/v1/research-a-development/internal--external-funding/2011-funding.html" class="mega" id="menu168" title="2011 Funding"><span class="menu-title">2011 Funding</span></a></li><li class="mega"><a href="/v1/research-a-development/internal--external-funding/2010-funding.html" class="mega" id="menu169" title="2010 Funding"><span class="menu-title">2010 Funding</span></a></li><li class="mega"><a href="/v1/research-a-development/internal--external-funding/2009-funding.html" class="mega" id="menu170" title="2009 Funding"><span class="menu-title">2009 Funding</span></a></li><li class="mega"><a href="/v1/research-a-development/internal--external-funding/2008-funding.html" class="mega" id="menu171" title="2008 Funding"><span class="menu-title">2008 Funding</span></a></li><li class="mega last"><a href="/v1/research-a-development/internal--external-funding/2007-funding.html" class="mega last" id="menu172" title="2007 Funding"><span class="menu-title">2007 Funding</span></a></li></ul></div></div>
</div></div></li><li class="mega"><a href="http://rmi.uitm.edu.my/" target="_blank" class="mega" id="menu123" title="Research Management Institute (RMI)"><span class="menu-title">Research Management Institute (RMI)</span></a></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu126" title="Research/Invention &amp; Innovation  Awards"><span class="menu-title">Research/Invention &amp; Innovation  Awards</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 120px;"><div class="megacol column1 first" style="width: 120px;"><ul class="megamenu level2"><li class="mega first"><a href="/v1/research-a-development/research-awards/year-2013.html" class="mega first" id="menu173" title="Year 2013"><span class="menu-title">Year 2013</span></a></li><li class="mega"><a href="/v1/research-a-development/research-awards/2012.html" class="mega" id="menu127" title="Year 2012"><span class="menu-title">Year 2012</span></a></li><li class="mega"><a href="/v1/research-a-development/research-awards/2011.html" class="mega" id="menu128" title="Year 2011"><span class="menu-title">Year 2011</span></a></li><li class="mega"><a href="/v1/research-a-development/research-awards/2010.html" class="mega" id="menu129" title="Year 2010"><span class="menu-title">Year 2010</span></a></li><li class="mega"><a href="/v1/research-a-development/research-awards/2009.html" class="mega" id="menu130" title="Year 2009"><span class="menu-title">Year 2009</span></a></li><li class="mega"><a href="/v1/research-a-development/research-awards/2008.html" class="mega" id="menu131" title="Year 2008"><span class="menu-title">Year 2008</span></a></li><li class="mega"><a href="/v1/research-a-development/research-awards/2007.html" class="mega" id="menu132" title="Year 2007"><span class="menu-title">Year 2007</span></a></li><li class="mega last"><a href="/v1/research-a-development/research-awards/2006.html" class="mega last" id="menu133" title="Year 2006"><span class="menu-title">Year 2006</span></a></li></ul></div></div>
</div></div></li><li class="mega last"><a href="/v1/research-a-development/mou-uitm-dosm.html" class="mega last" id="menu217" title="MoU UiTM - DOSM"><span class="menu-title">MoU UiTM - DOSM</span></a></li></ul></div></div>
</div></div></li><li class="mega haschild"><a href="#" class="mega haschild" id="menu64" title="Student"><span class="menu-title">Student</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 220px;"><div class="megacol column1 first" style="width: 220px;"><ul class="megamenu level1"><li class="mega first"><a href="/v1/student/clubs-a-societies.html" class="mega first" id="menu116" title="Clubs &amp; Societies"><span class="menu-title">Clubs &amp; Societies</span></a></li><li class="mega"><a href="http://hep1.uitm.edu.my/" target="_blank" class="mega" id="menu163" title="UiTM Student Affairs Division"><span class="menu-title">UiTM Student Affairs Division</span></a></li><li class="mega haschild"><a href="/v1/student/fskm-office-of-student-affairs.html" class="mega haschild" id="menu165" title="FSKM Office of Student Affairs"><span class="menu-title">FSKM Office of Student Affairs</span></a><div class="childcontent cols1 ">
<div class="childcontent-inner-wrap">
<div class="childcontent-inner clearfix" style="width: 285px;"><div class="megacol column1 first" style="width: 285px;"><ul class="megamenu level2"><li class="mega first"><a href="/v1/student/fskm-office-of-student-affairs/ke-arah-kecemerlangan-akademikkaca.html" class="mega first" id="menu189" title="Ke Arah keCemerlangan Akademik (KACA)"><span class="menu-title">Ke Arah keCemerlangan Akademik (KACA)</span></a></li><li class="mega"><a href="/v1/student/fskm-office-of-student-affairs/fskm-sport-carnival-2013.html" class="mega" id="menu190" title="FSKM Sport Carnival 2013"><span class="menu-title">FSKM Sport Carnival 2013</span></a></li><li class="mega"><a href="/v1/student/fskm-office-of-student-affairs/tahniah-bakal-graduan.html" class="mega" id="menu191" title="Tahniah Bakal Graduan"><span class="menu-title">Tahniah Bakal Graduan</span></a></li><li class="mega last"><a href="/v1/student/fskm-office-of-student-affairs/perkhemahan-perdana-fskm-2013.html" class="mega last" id="menu192" title="Perkhemahan Perdana FSKM 2013"><span class="menu-title">Perkhemahan Perdana FSKM 2013</span></a></li></ul></div></div>
</div></div></li><li class="mega"><a href="/v1/student/kemahiran-insaniah-pro-ki.html" class="mega" id="menu167" title="Kemahiran Insaniah (Pro-KI)"><span class="menu-title">Kemahiran Insaniah (Pro-KI)</span></a></li><li class="mega last"><a href="/v1/student/download.html" class="mega last" id="menu158" title="Download"><span class="menu-title">Download</span></a></li></ul></div></div>
</div></div></li><li class="mega"><a href="/v1/advisor.html" class="mega" id="menu157" title="Advisor"><span class="menu-title">Advisor</span></a></li><li class="mega last"><a href="/v1/gallery.html" class="mega last" id="menu159" title="Gallery"><span class="menu-title">Gallery</span></a></li></ul>
</div>

			<script type="text/javascript">

			var megamenu = new ruMegaMenuMoo ('ru-mainnav', {

				'bgopacity': 0, 

				'delayHide': 1000, 

				'slide': 1, 


				'fading': 1,


				'direction':'down',


				'action':'mouseover',


				'tips': false,


				'duration': 300,


				'hidestyle': 'fastwhenshow'


			});			


			</script>


	

	</div>


	</div>


</div>










<ul class="no-display">


    <li><a href="/v1/fakulti/staff-directory/academic/1097.html#ru-content" title="Skip to content">Skip to content</a></li>


</ul>







	<!-- //MAIN NAVIGATION -->





	









	<!-- MAIN CONTAINER -->


	<div id="ru-container" class="wrap ">


	<div class="main clearfix">





		<div id="ru-mainbody" style="width:100%">


			<div class="ru-navhelper wrap">


<div class="main clearfix">


	<div class="inner clearfix">


		<div class="ru-breadcrums">
			<!--ru Template Guide only-->
			<strong>HOME:</strong>

<span class="breadcrumbs pathway">


<span class="name">Faculty</span> <img src="/v1/templates/ru_upwh2010/images/arrow.png" alt=""  /> <span class="name">Staff Directory</span> <img src="/v1/templates/ru_upwh2010/images/arrow.png" alt=""  /> <span class="name">Academic</span>

</span>

		</div>
		<ul class="no-display">
			<li><a href="/v1/fakulti/staff-directory/academic/1097.html#ru-content" title="Skip to content">Skip to content</a></li>

		</ul>
	</div>
</div>
</div>




			<!-- CONTENT -->


<div id="ru-main" style="width:100%">


<div class="inner clearfix">


	





	




	<div id="ru-contentwrap" class=" clearfix">


		

			<div id="ru-content" class="column" style="width:100%">


	


				<div id="ru-current-content" class="column" style="width:100%">


					

					


					

					<div class="ru-content-main clearfix">


						
















<h2 class="contentheading clearfix">


	

		Computer Sciences Lecturer

	



</h2>












<div class="article-tools clearfix">


	<div class="article-meta">


	

		<span class="createdate">


			Friday, 18 January 2013 16:00

		</span>


	




	







	

	</div>


	


	

	<div class="buttonheading">


		

			

			<span>


			<a href="/v1/component/mailto/?tmpl=component&amp;link=f94ed89a8107dd4143748aff4662573181425b36" title="E-mail" onclick="window.open(this.href,'win2','width=400,height=350,menubar=yes,resizable=yes'); return false;"><img src="/v1/templates/ru_upwh2010/images/emailButton.png" alt="E-mail"  /></a>

			</span>


			




			

			<span>


			<a href="/v1/fakulti/staff-directory/academic/1097-computer-sciences-lecturer.html?tmpl=component&amp;print=1&amp;page=" title="Print" onclick="window.open(this.href,'win2','status=no,toolbar=no,scrollbars=yes,titlebar=no,menubar=no,resizable=yes,width=640,height=480,directories=no,location=no'); return false;" rel="nofollow"><img src="/v1/templates/ru_upwh2010/images/printButton.png" alt="Print"  /></a>

			</span>


			




			

			<span>


			<a href="/v1/fakulti/staff-directory/academic/1097-computer-sciences-lecturer.pdf" title="PDF" onclick="window.open(this.href,'win2','status=no,toolbar=no,scrollbars=yes,titlebar=no,menubar=no,resizable=yes,width=640,height=480,directories=no,location=no'); return false;" rel="nofollow"><img src="/v1/templates/ru_upwh2010/images/pdf_button.png" alt="PDF"  /></a>

			</span>


			

		

	</div>


	




	

	


</div>












<div class="article-content">




<table id="mytable" border="0" cellspacing="0" summary="The technical  specifications of the Apple PowerMac G5 series">
<caption> </caption> 
<tbody>
<tr align="left" valign="middle">
<th width="20" scope="col">#</th><th style="width: 310px;" scope="col">Name</th><th style="width: 90px;" scope="col">Position</th><th style="width: 210px;" scope="col">Contact</th><th style="width: 280px;" scope="col">Expertise</th>
</tr>
<tr align="left" valign="middle">
<td><strong>1 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1460478621" href="/v1/fakulti/staff-directory/academic/757.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Afiza Ismail</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer<br /></strong></td>
<td><strong>603-55211159 <br /></strong><span style="color: #c75f3e;"><strong>
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy41090 = 'f&#105;z&#97;' + '&#64;';
 addy41090 = addy41090 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy41090 + suffix + '\'' + attribs + '>' );
 document.write( addy41090 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></strong></span></td>
<td><strong>-Programming<br />-Computer Science Education<br /></strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>2 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_2144405360" href="/v1/fakulti/staff-directory/academic/758.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Ali Seman (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong><strong>Senior Lecturer</strong></strong></td>
<td><strong>603-55211168 <br /></strong><span style="color: #c75f3e;"><strong>
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy53679 = '&#97;l&#105;s&#101;m&#97;n' + '&#64;';
 addy53679 = addy53679 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy53679 + suffix + '\'' + attribs + '>' );
 document.write( addy53679 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></strong></span></td>
<td><strong>-Bioinformatics<br />-Computational Molecular Biology<span style="font-weight: normal;"> </span></strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>3</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1241555166" href="/v1/fakulti/staff-directory/academic/605.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Azizian Mohd Sapawi</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Lecturer</strong></td>
<td><strong>603-55211165 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy35516 = '&#97;z&#105;z&#105;&#97;n' + '&#64;';
 addy35516 = addy35516 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy35516 + suffix + '\'' + attribs + '>' );
 document.write( addy35516 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Bioinformatics</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>4 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_22664105" href="/v1/fakulti/staff-directory/academic/756.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Azlan Abdul Aziz</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer</strong></td>
<td><strong>603-55211167 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy1002 = '&#97;zl&#97;n&#97;&#97;' + '&#64;';
 addy1002 = addy1002 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy1002 + suffix + '\'' + attribs + '>' );
 document.write( addy1002 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Multimedia Education<br /> -Multimedia Learning Technology</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>5 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_94412698" href="/v1/fakulti/staff-directory/academic/754.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Azlan Ismail (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer</strong></td>
<td><strong>603-55211183 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy83360 = '&#97;zl&#97;n&#105;sm&#97;&#105;l' + '&#64;';
 addy83360 = addy83360 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy83360 + suffix + '\'' + attribs + '>' );
 document.write( addy83360 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Web Services<br /> -Service Oriented Computing</strong><strong><br /> -Autonomic Computing<br /> -Software Engineering</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>6 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1868602996" href="/v1/fakulti/staff-directory/academic/515.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Fakhrul Hazman Mohd Yusoff (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211136 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy31128 = 'f&#97;khr&#117;l' + '&#64;';
 addy31128 = addy31128 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy31128 + suffix + '\'' + attribs + '>' );
 document.write( addy31128 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Computer Graphic<br /> -Vision<br /> -Visualization</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>7</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_2103415900" href="/v1/fakulti/staff-directory/academic/753.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Fazilah Ismail</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211134 <br /><span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy55958 = 'f&#97;z&#105;l&#97;h' + '&#64;';
 addy55958 = addy55958 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy55958 + suffix + '\'' + attribs + '>' );
 document.write( addy55958 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span> </strong></td>
<td><strong>-Human Computer Interaction<br /> -Multimedia</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>8</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_411111331" href="/v1/fakulti/staff-directory/academic/592.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Hani Fuziah Abdul Rahman </strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211186 <br /><span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy40219 = 'h&#97;n&#105;' + '&#64;';
 addy40219 = addy40219 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy40219 + suffix + '\'' + attribs + '>' );
 document.write( addy40219 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span> </strong></td>
<td><strong>-Programming<br />-System Dynamic</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>9 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1512803071" href="/v1/fakulti/staff-directory/academic/750.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Haslizatul Fairuz Mohamed Hanum</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Lecturer </strong></td>
<td><strong>603-55211157 <br /><span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy8370 = 'f&#97;&#105;r&#117;z' + '&#64;';
 addy8370 = addy8370 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy8370 + suffix + '\'' + attribs + '>' );
 document.write( addy8370 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Programming &amp; Algorithms<br />-Parallel Algorithms, Retrieval Algorithms</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>10 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1804866100" href="/v1/fakulti/staff-directory/academic/749.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Hayati Abd Rahman (Dr.)</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer</strong></td>
<td><strong>603-55211123 <br /><span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy23171 = 'h&#97;y&#97;t&#105;&#97;r' + '&#64;';
 addy23171 = addy23171 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy23171 + suffix + '\'' + attribs + '>' );
 document.write( addy23171 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span> </strong></td>
<td><strong>-Web Semantics</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>11 </strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1061838666" href="/v1/fakulti/staff-directory/academic/745.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Khalil Hj. Awang (Assoc. Prof.) </strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong>Assoc. Prof.</strong></td>
<td align="left" valign="middle"><strong>603-55435307 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy70298 = 'kh&#97;l&#105;l' + '&#64;';
 addy70298 = addy70298 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy70298 + suffix + '\'' + attribs + '>' );
 document.write( addy70298 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Programming<br /> -Computer Education</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>12 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_402242447" href="/v1/fakulti/staff-directory/academic/743.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Marina Ismail (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211135<br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy38874 = 'm&#97;r&#105;n&#97;' + '&#64;';
 addy38874 = addy38874 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy38874 + suffix + '\'' + attribs + '>' );
 document.write( addy38874 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Game Based Learning<br /> -Computer Science Education<br /> -Multimedia Pedagogial Agent</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>13 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1159050453" href="/v1/fakulti/staff-directory/academic/742.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Marshima Mohd Rosli</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer <strong>(Study Leave)</strong></strong></td>
<td><strong>603-55211192<br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy58393 = 'm&#97;rsh&#105;m&#97;' + '&#64;';
 addy58393 = addy58393 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy58393 + suffix + '\'' + attribs + '>' );
 document.write( addy58393 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Web Programming &amp; Application<br /> -Software Testing<br /> -Configuration Management</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>14 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_406925821" href="/v1/fakulti/staff-directory/academic/741.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Mohd Nor Hajar Hasrol Jono </strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer</strong></td>
<td><strong>603-55211118 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy233 = 'h&#97;sr&#111;l' + '&#64;';
 addy233 = addy233 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy233 + suffix + '\'' + attribs + '>' );
 document.write( addy233 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Multimedia Aplication<br /> -E-Learning</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>15 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_419595576" href="/v1/fakulti/staff-directory/academic/740.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Mohd Suffian Bin Sulaiman</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer </strong></td>
<td><strong>603-55211125 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy27192 = 's&#117;ff&#105;&#97;n' + '&#64;';
 addy27192 = addy27192 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy27192 + suffix + '\'' + attribs + '>' );
 document.write( addy27192 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Software Engineering<br /> -Mobile Application</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>16 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1789183350" href="/v1/fakulti/staff-directory/academic/613.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Mohd Yunus Mohd Yussof </strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211137 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy94670 = 'mymy' + '&#64;';
 addy94670 = addy94670 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy94670 + suffix + '\'' + attribs + '>' );
 document.write( addy94670 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Opensource Aplication<br /> -Multimedia</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>17 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1265376228" href="/v1/fakulti/staff-directory/academic/739.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Muthukkaruppan Annamalai<br /> (Assoc. Prof. Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Assoc. Prof. </strong></td>
<td><strong>603-55211161 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy34564 = 'mk' + '&#64;';
 addy34564 = addy34564 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy34564 + suffix + '\'' + attribs + '>' );
 document.write( addy34564 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Knowledge / Informat ion Modelling<br /> -Ontology Engineering</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>18</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_665072834" href="/v1/fakulti/staff-directory/academic/589.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Nasiroh Omar (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer</strong></td>
<td><strong>603-55211172<br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy2524 = 'n&#97;s&#105;r&#111;h' + '&#64;';
 addy2524 = addy2524 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy2524 + suffix + '\'' + attribs + '>' );
 document.write( addy2524 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Networked Collaborative Environment<br /> -Computer-Based Bahavior<br /> -Visualization</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>19</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1299566469" href="/v1/fakulti/staff-directory/academic/738.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Nazrul Azha Hj. Mohamed Shaari (Dr.)</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211117 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy28895 = 'n&#97;sh' + '&#64;';
 addy28895 = addy28895 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy28895 + suffix + '\'' + attribs + '>' );
 document.write( addy28895 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Virtual Learning Environment<br /> -Virtual Reality</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>20 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1294840380" href="/v1/fakulti/staff-directory/academic/737.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><span style="color: #c75f3e;"><strong>Noor Elaiza Abd. Khalid </strong></span></span><span style="color: #800080;"><strong><span style="color: #c75f3e;">(Dr.)</span> </strong></span><span style="color: #800080;"><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer</strong></td>
<td><strong>603-55211164 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy88039 = '&#101;l&#97;&#105;z&#97;' + '&#64;';
 addy88039 = addy88039 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy88039 + suffix + '\'' + attribs + '>' );
 document.write( addy88039 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Swarm intelligence &amp; Fuzzy Techniques<br /> -</strong><strong>Evolutionary computing algorithms<br /> -Medical imaging</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>21</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_830255499" href="/v1/fakulti/staff-directory/academic/735.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Noor Latiffah Adam</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer </strong></td>
<td><strong>603-55211157 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy48301 = 'l&#97;t&#105;ff&#97;h' + '&#64;';
 addy48301 = addy48301 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy48301 + suffix + '\'' + attribs + '>' );
 document.write( addy48301 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Programming<br /> -Machine Learning</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>21 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_417502550" href="/v1/fakulti/staff-directory/academic/555.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Nor Ashikin Mohd Kamal</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Lecturer <strong>(Study Leave)</strong></strong></td>
<td><strong>603-55211169</strong><span style="color: #c75f3e;"><strong><br /> 
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy47166 = 'n&#111;r_&#97;sh&#105;k&#105;n' + '&#64;';
 addy47166 = addy47166 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy47166 + suffix + '\'' + attribs + '>' );
 document.write( addy47166 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></strong></span></td>
<td><strong>-Image Processing<br /> -Programming</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>23</strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1286599358" href="/v1/fakulti/staff-directory/academic/732.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Noraini Seman (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong>Senior<br /> Lecturer<br /> </strong></td>
<td align="left" valign="middle"><strong>603-55211127 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy90960 = '&#97;&#105;n&#105;' + '&#64;';
 addy90960 = addy90960 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy90960 + suffix + '\'' + attribs + '>' );
 document.write( addy90960 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Speech Recognition<br /> -Digital Signal Processing<br /> -Artificial Intelligence</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>24 </strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_637397768" href="/v1/fakulti/staff-directory/academic/731.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Norasiah Mohammad</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong>Senior<br /> Lecturer</strong></td>
<td align="left" valign="middle"><strong>603-55211158 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy12808 = 'n&#111;r&#97;s&#105;&#97;h' + '&#64;';
 addy12808 = addy12808 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy12808 + suffix + '\'' + attribs + '>' );
 document.write( addy12808 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Computer Sciences Education<br /> -Multimedia</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>25 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_2053254738" href="/v1/fakulti/staff-directory/academic/729.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Noratikah Shamsudin</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer</strong></td>
<td><strong>603-55211171 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy19409 = '&#97;t&#105;k&#97;h' + '&#64;';
 addy19409 = addy19409 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy19409 + suffix + '\'' + attribs + '>' );
 document.write( addy19409 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Programming Language<br /> -Computer Sciences Education</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>26</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1180181170" href="/v1/fakulti/staff-directory/academic/728.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Nordin Abu Bakar (Assoc. Prof. Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Assoc. Prof. </strong></td>
<td><strong>603-55211162 (O), <br /> 603-55199010 (H),<br /> 019-9859010 (HP)<br /></strong><strong> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy12830 = 'n&#111;rd&#105;n' + '&#64;';
 addy12830 = addy12830 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy12830 + suffix + '\'' + attribs + '>' );
 document.write( addy12830 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong><br /></td>
<td><strong>-Artificial Intelligence<br /> -Genetic  Algorithms<br /> -Software Engineering</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>27 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1221044914" href="/v1/fakulti/staff-directory/academic/593.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Norizan Mat Diah</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer </strong></td>
<td><strong>603-55211184 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy96855 = 'n&#111;r&#105;z&#97;nm' + '&#64;';
 addy96855 = addy96855 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy96855 + suffix + '\'' + attribs + '>' );
 document.write( addy96855 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Computer Games<br /> -Multimedia Education<br /> -Educational Computer Games</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>28 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1658754303" href="/v1/fakulti/staff-directory/academic/727.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Normaly Kamal Ismail (Dr.)</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211156 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy74968 = 'n&#111;rm&#97;ly' + '&#64;';
 addy74968 = addy74968 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy74968 + suffix + '\'' + attribs + '>' );
 document.write( addy74968 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Programming<br /> -Information Storage &amp; Retrieval</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>29 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1443388299" href="/v1/fakulti/staff-directory/academic/726.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Norzehan Sakamat</strong></span><strong>
				  </a></div></strong></td>
<td><strong>Senior<br /> Lecturer </strong></td>
<td><strong>603-55211160 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy93623 = 'z&#101;h&#97;n' + '&#64;';
 addy93623 = addy93623 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy93623 + suffix + '\'' + attribs + '>' );
 document.write( addy93623 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Programming<br /> -Decision Support System Using Fuzzy Logic Inter Ference Engine</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>30 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_645924747" href="/v1/fakulti/staff-directory/academic/725.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Norzilah Musa</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer </strong></td>
<td><strong>603-55211175 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy11872 = 'n&#111;rz&#105;l&#97;h' + '&#64;';
 addy11872 = addy11872 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy11872 + suffix + '\'' + attribs + '>' );
 document.write( addy11872 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Programming<br /> -Object Oriented Paradigm</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>31 </strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_655060151" href="/v1/fakulti/staff-directory/academic/724.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Nur Atiqah Sia Abdullah @ Sia Sze Yieng (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong>Senior<br /> Lecturer<br /> </strong></td>
<td align="left" valign="middle"><strong>603-55211175 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy91042 = '&#97;t&#105;q&#97;h' + '&#64;';
 addy91042 = addy91042 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy91042 + suffix + '\'' + attribs + '>' );
 document.write( addy91042 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Software Engineering<br /> -Software Metrics</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>32</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_756383272" href="/v1/fakulti/staff-directory/academic/722.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Nurazzah Abdul Rahman<br /> (Assoc. Prof. Dr.)</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Assoc. Prof. </strong></td>
<td><strong>603-55211197 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy34712 = 'n&#117;r&#97;zz&#97;h' + '&#64;';
 addy34712 = addy34712 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy34712 + suffix + '\'' + attribs + '>' );
 document.write( addy34712 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-High Performance Computing<br /> -Information Storage &amp; Retrieval</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>33</strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_642846459" href="/v1/fakulti/staff-directory/academic/720.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Nursuriati Jamil (Assoc. Prof. Dr.)</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong>Assoc. Prof.</strong></td>
<td align="left" valign="middle"><strong>603-55211198<br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy65551 = 'l&#105;z&#97;' + '&#64;';
 addy65551 = addy65551 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy65551 + suffix + '\'' + attribs + '>' );
 document.write( addy65551 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Multimedia Information Retrieval<br /> -Signal &amp; Image Processing<br /></strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>34 </strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1896615318" href="/v1/fakulti/staff-directory/academic/717.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><span style="color: #c75f3e;"><strong>Riaza Perveen Mohd Rias</strong><strong> </strong></span></span><span style="color: #c75f3e;"><strong>(Dr.)</strong></span><span style="color: #800080;"><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong>Senior</strong> <strong>Lecturer<br /> </strong></td>
<td align="left" valign="middle"><strong>603-55211130 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy26558 = 'r&#105;&#97;z&#97;' + '&#64;';
 addy26558 = addy26558 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy26558 + suffix + '\'' + attribs + '>' );
 document.write( addy26558 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Multimedia Based Research<br /> -Mobile Application<br /> -Interface Design</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>35</strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_779047377" href="/v1/fakulti/staff-directory/academic/620.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						<span style="color: #c75f3e;"><strong>Rosmah Abdul Latif (Assoc. Prof.)</strong></span><span style="color: #333333;"><strong> 
				  </a></div></strong></span></strong></span></span></td>
<td align="left" valign="middle"><strong>Assoc. Prof.<br /> </strong></td>
<td align="left" valign="middle"><strong>603-55211180<br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy35714 = 'r&#111;s&#101;' + '&#64;';
 addy35714 = addy35714 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy35714 + suffix + '\'' + attribs + '>' );
 document.write( addy35714 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Programming<br /> -Computer Sciences Education</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>36</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_737259158" href="/v1/fakulti/staff-directory/academic/715.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Rose Hafsah Abd Rauf (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211182<br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy48910 = 'r&#111;s&#101;h&#97;fs&#97;h' + '&#64;';
 addy48910 = addy48910 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy48910 + suffix + '\'' + attribs + '>' );
 document.write( addy48910 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Steganography<br /> -Computer Forensics<br /> -Forensic Science (Blood Spatter Analysis)</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>37</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1617734666" href="/v1/fakulti/staff-directory/academic/713.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Rosmawati Nordin (Assoc. Prof. Dr.)</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Assoc. Prof. </strong></td>
<td><strong>603-55211181 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy57686 = 'r&#111;sw&#97;t&#105;' + '&#64;';
 addy57686 = addy57686 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy57686 + suffix + '\'' + attribs + '>' );
 document.write( addy57686 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-CS Algorithm<br /> -Software Enginnering<br /> -CS Education</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>38 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_734979629" href="/v1/fakulti/staff-directory/academic/712.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Rosslina Mohamed Nawi (Assoc. Prof.)</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Assoc. Prof.</strong></td>
<td><strong>603-55211189 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy91671 = 'r&#111;ssl&#105;n&#97;' + '&#64;';
 addy91671 = addy91671 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy91671 + suffix + '\'' + attribs + '>' );
 document.write( addy91671 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Multimedia<br /> -Web Programming</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>39 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1148370489" href="/v1/fakulti/staff-directory/academic/519.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Sharifah Aliman</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer<br /> </strong></td>
<td><strong>603-55211118<br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy89129 = 'sh&#97;r&#105;f&#97;h&#97;l&#105;' + '&#64;';
 addy89129 = addy89129 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy89129 + suffix + '\'' + attribs + '>' );
 document.write( addy89129 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td>-<strong>Programming, Social Media and Multimedia</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>40 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_983054089" href="/v1/fakulti/staff-directory/academic/551.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						<span style="color: #c75f3e;">Sharifalillah Nordin </span></strong></span><strong><span style="color: #c75f3e;">(Dr.)</span> </strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer</strong></td>
<td><strong>603-55211126</strong><br /> <span style="color: #c75f3e;"><strong>
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy66056 = 'sh&#97;r&#105;f&#97;' + '&#64;';
 addy66056 = addy66056 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy66056 + suffix + '\'' + attribs + '>' );
 document.write( addy66056 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></strong></span></td>
<td><strong>-Artificial Intelligence<br /> -Bioinformatics</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>41</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_392362081" href="/v1/fakulti/staff-directory/academic/711.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Siti Salwa binti Salleh (Dr.) </strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211132 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy14842 = 'ss&#97;lw&#97;' + '&#64;';
 addy14842 = addy14842 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy14842 + suffix + '\'' + attribs + '>' );
 document.write( addy14842 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Multimedia Signal Processing<br /> -Geometric Visualisation &amp; Modeling<br /> -Computer Generated Imagery</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>42 </strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_62725507" href="/v1/fakulti/staff-directory/academic/710.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Siti Zaleha Zainal Abidin (Assoc. Prof. Dr.)</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong>Assoc. Prof. </strong></td>
<td align="left" valign="middle"><strong>603-55211187 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy59426 = 'z&#97;l&#101;h&#97;' + '&#64;';
 addy59426 = addy59426 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy59426 + suffix + '\'' + attribs + '>' );
 document.write( addy59426 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Interactive Computing<br /> -Languange Construction, Collaborative Networked Environment</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>43 </strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1385296537" href="/v1/fakulti/staff-directory/academic/709.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Suriyani Ariffin (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong>Senior Lecturer</strong></td>
<td align="left" valign="middle"><strong>603-55211174 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy4929 = 's&#117;r&#105;y&#97;n&#105;' + '&#64;';
 addy4929 = addy4929 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy4929 + suffix + '\'' + attribs + '>' );
 document.write( addy4929 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-<strong>Programming</strong><br /> -Information Security<br /> -Cryptographic Algorithm<br /></strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>44 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1551412535" href="/v1/fakulti/staff-directory/academic/638.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Suzana binti Ahmad</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Senior<br /> Lecturer</strong></td>
<td><strong>603-55211169 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy73234 = 's&#117;z&#97;n&#97;' + '&#64;';
 addy73234 = addy73234 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy73234 + suffix + '\'' + attribs + '>' );
 document.write( addy73234 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Collaborative Networked Environment<br /> -Multimedia Educational Game</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>45 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_469651328" href="/v1/fakulti/staff-directory/academic/706.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Syed Ahmad Sheikh Aljunid<br /> (Assoc. Prof. Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><br /><strong>Assoc. Prof. </strong></td>
<td><strong>603-55211196 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy59658 = '&#97;lj&#117;n&#105;d' + '&#64;';
 addy59658 = addy59658 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy59658 + suffix + '\'' + attribs + '>' );
 document.write( addy59658 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Computer Science Education (Programming Pedagogy)<br /> -Watermarking and Steganography<br /> -Mobile and Cloud Computing</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>46 </strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1804892113" href="/v1/fakulti/staff-directory/academic/705.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Wan Ya bin Wan Hussin</strong><span style="color: #333333;"><strong> 
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer</strong></td>
<td><strong>603-55211124 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy32121 = 'w&#97;ny&#97;' + '&#64;';
 addy32121 = addy32121 + 's&#97;l&#97;m' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy32121 + suffix + '\'' + attribs + '>' );
 document.write( addy32121 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Software Engineering<br /> -Programming<br /> -Database</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>47</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1193112237" href="/v1/fakulti/staff-directory/academic/704.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Zaidah Ibrahim (Assoc. Prof.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Assoc. Prof. <br /></strong></td>
<td><strong>603-55211151 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy67904 = 'z&#97;&#105;d&#97;h' + '&#64;';
 addy67904 = addy67904 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy67904 + suffix + '\'' + attribs + '>' );
 document.write( addy67904 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Computational Intelligent<br /> -Image Processing</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>48</strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_1735027557" href="/v1/fakulti/staff-directory/academic/895.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Zainab Abu Bakar (Prof. Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong> Prof. Dr.</strong></td>
<td align="left" valign="middle"><strong>603-55211200 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy94222 = 'z&#97;&#105;n&#97;b' + '&#64;';
 addy94222 = addy94222 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy94222 + suffix + '\'' + attribs + '>' );
 document.write( addy94222 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Information Retrieval<br /> -Semantic Web</strong></td>
</tr>
<tr>
<td align="left" valign="middle"><strong>49</strong></td>
<td align="left" valign="middle"><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_322481299" href="/v1/fakulti/staff-directory/academic/702.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Zalilah Abd Aziz (Dr.)</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td align="left" valign="middle"><strong>Senior Lecturer<br /> </strong></td>
<td align="left" valign="middle"><strong>603-55211127 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy34644 = 'z&#97;l&#105;l&#97;h' + '&#64;';
 addy34644 = addy34644 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy34644 + suffix + '\'' + attribs + '>' );
 document.write( addy34644 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td align="left" valign="middle"><strong>-Metaheuristics &amp; Optimization<br /> -Combinatorial Optimization Problems</strong></td>
</tr>
<tr align="left" valign="middle">
<td><strong>50</strong></td>
<td><span style="color: #800080;"><span style="color: #333333;"><strong><div><a id="href_345195058" href="/v1/fakulti/staff-directory/academic/701.html?tmpl=component" 
						onclick="if(!hs.htmlExpand(this, { objectType:'iframe',outlineType:'rounded-white',width:800,height:450  } )) return false;">
						</strong></span><strong>Zulaile Mabni</strong><span style="color: #333333;"><strong>
				  </a></div></strong></span></span></td>
<td><strong>Senior Lecturer<br /></strong></td>
<td><strong>603-55211173 <br /> <span style="color: #c75f3e;">
 <script language='JavaScript' type='text/javascript'>
 <!--
 var prefix = 'm&#97;&#105;lt&#111;:';
 var suffix = '';
 var attribs = '';
 var path = 'hr' + 'ef' + '=';
 var addy96799 = 'z&#117;l&#97;&#105;l&#101;' + '&#64;';
 addy96799 = addy96799 + 'tmsk' + '&#46;' + '&#117;&#105;tm' + '&#46;' + '&#101;d&#117;' + '&#46;' + 'my';
 document.write( '<a ' + path + '\'' + prefix + addy96799 + suffix + '\'' + attribs + '>' );
 document.write( addy96799 );
 document.write( '<\/a>' );
 //-->
 </script><script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '<span style=\'display: none;\'>' );
 //-->
 </script>This e-mail address is being protected from spambots. You need JavaScript enabled to view it
 <script language='JavaScript' type='text/javascript'>
 <!--
 document.write( '</' );
 document.write( 'span>' );
 //-->
 </script></span></strong></td>
<td><strong>-Programming<br /> -Object Oriented Pradigm</strong></td>
</tr>
</tbody>
</table>

</div>







	<span class="modifydate">


		

	</span>












					</div>


					

	


					

				</div>


	


				

	


			</div>


			

	</div>


	


	

	


	<!-- CONTENT BOTTOM -->


	

	<!-- //CONTENT BOTTOM -->


	


</div>


</div>


<!-- //CONTENT -->

		</div>





		

		


	</div>
</div>
	<!-- //MAIN CONTAINER -->

	<!-- NAVHELPER -->

	<!-- //NAVHELPER -->

	

<!-- BOTTOM SPOTLIGHT -->


<div id="ru-botsl" class="wrap">


<div id="ru-botsl-inner1">


<div class="main clearfix">


	<div class="inner clearfix">





	

	<div class="ru-box column ru-box-full" style="width: 100%;">


		

	<div class="ru-moduletable moduletable  clearfix" id="Mod18">


		

		

		<h3 class="clearfix"><span>Login</span></h3>


		

		<div class="ru-box-ct clearfix">


		<form action="/v1/fakulti/staff-directory/academic.html" method="post" name="login" id="form-login" >
		<fieldset class="input">
	<p id="form-login-username">
		<label for="modlgn_username">Username</label><br />
		<input id="modlgn_username" type="text" name="username" class="inputbox" alt="username" size="18" />
	</p>
	<p id="form-login-password">
		<label for="modlgn_passwd">Password</label><br />
		<input id="modlgn_passwd" type="password" name="passwd" class="inputbox" size="18" alt="password" />
	</p>
		<p id="form-login-remember">
		<label for="modlgn_remember">Remember Me</label>
		<input id="modlgn_remember" type="checkbox" name="remember" class="inputbox" value="yes" alt="Remember Me" />
	</p>
		<input type="submit" name="Submit" class="button" value="Login" />
	</fieldset>
	
>>> 

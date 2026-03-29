import os

base_folder = r"D:\all_media\photos"
output_file = r"D:\all_media\index.html"

html_start = """
<html>
<head>
<title>My Photo Gallery</title>
<style>
body{font-family:Arial}
img{margin:5px;border-radius:8px}
.gallery{display:flex;flex-wrap:wrap}
</style>

<script>
function filterGallery(){
    var year=document.getElementById("year").value;
    var month=document.getElementById("month").value;
    var imgs=document.getElementsByClassName("photo");

    for(let i=0;i<imgs.length;i++){
        let y=imgs[i].getAttribute("data-year");
        let m=imgs[i].getAttribute("data-month");

        if((year=="all"||year==y)&&(month=="all"||month==m)){
            imgs[i].style.display="block";
        }else{
            imgs[i].style.display="none";
        }
    }
}
</script>

</head>
<body>

<h2>My Photo Gallery</h2>

Year:
<select id="year" onchange="filterGallery()">
<option value="all">All</option>
"""

html_middle = ""
years=set()
months=set()

for year in os.listdir(base_folder):
    year_path=os.path.join(base_folder,year)
    if os.path.isdir(year_path):
        years.add(year)
        for month in os.listdir(year_path):
            month_path=os.path.join(year_path,month)
            if os.path.isdir(month_path):
                months.add(month)

html_years=""
for y in sorted(years):
    html_years+=f'<option value="{y}">{y}</option>'

html_month="""
</select>

Month:
<select id="month" onchange="filterGallery()">
<option value="all">All</option>
"""

for m in sorted(months):
    html_month+=f'<option value="{m}">{m}</option>'

html_month+="</select><hr><div class='gallery'>"

html_images=""

for year in os.listdir(base_folder):
    year_path=os.path.join(base_folder,year)
    if os.path.isdir(year_path):
        for month in os.listdir(year_path):
            month_path=os.path.join(year_path,month)
            if os.path.isdir(month_path):
                for file in os.listdir(month_path):
                    if file.lower().endswith((".jpg",".jpeg",".png",".webp")):
                        path=f"photos/{year}/{month}/{file}"
                        html_images+=f'''
<img class="photo" src="{path}" data-year="{year}" data-month="{month}" width="300" loading="lazy">
'''

html_end="""
</div>
</body>
</html>
"""

with open(output_file,"w",encoding="utf8") as f:
    f.write(html_start)
    f.write(html_years)
    f.write(html_month)
    f.write(html_images)
    f.write(html_end)

print("Gallery created successfully!")
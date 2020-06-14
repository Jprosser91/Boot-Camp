#create a directory for JPG PNG & TIFF Files
mkdir JPG PNG TIFF 
# Find all JPG Files and move them into JPG
find . -iname '*.jpg' -exec cp {} JPG \; 2>/dev/null
#Find all PNG Files and move them into PNG
find . -iname '*.png' -exec cp {} PNG \; 2>/dev/null
#Find all TIFF Files and Move them into TIFF
find . -iname '*.tiff' -exec cp {} TIFF \; 2>/dev/null
#Create a new file called PictureCounts.md
touch PictureCounts.md
#Count how many times JPG occurs and Append the number to PictureCounts.md
echo JPG: > PictureCounts.md | ls -1 JPG/ | wc -l >> PictureCounts.md 
#Count how many times PNG occurs and append the number to PictureCounts.md
echo PNG: >> PictureCounts.md | ls -1 PNG/ | wc -l >> PictureCounts.md
#Count how many time TIFF occurs and append the number to PictureCounts.md
echo TIFF: >> PictureCounts.md | ls -1 TIFF/ | wc -l >> PictureCounts.md
#End Script
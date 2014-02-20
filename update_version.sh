BASE_STRING=`cat VERSION`
BASE_LIST=(`echo $BASE_STRING | tr '.' ' '`)
V_MAJOR=${BASE_LIST[0]}
V_MINOR=${BASE_LIST[1]}
V_PATCH=${BASE_LIST[2]}
echo "Current version : $BASE_STRING"
V_MINOR=$((V_MINOR + 1))
V_PATCH=0
SUGGESTED_VERSION="$V_MAJOR.$V_MINOR.$V_PATCH"
INPUT_STRING=$SUGGESTED_VERSION
echo "Will set new version to be $INPUT_STRING"
echo $INPUT_STRING > VERSION
#echo "Version $INPUT_STRING:" > tmpfile
#git log --pretty=format:" - %s" "v$BASE_STRING"...HEAD >> tmpfile
#echo "" >> tmpfile
#echo "" >> tmpfile
#cat CHANGES >> tmpfile
#mv tmpfile CHANGES
#git add CHANGES VERSION
git add VERSION
git commit -m "Version bump to $INPUT_STRING"
git tag -a -m "Tagging version $INPUT_STRING" "v$INPUT_STRING"
#git push origin --tags
#git push
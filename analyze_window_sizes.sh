if [ ! -d "./recolected_info"  ]; then
  mkdir recolected_info
fi
if [ ! -d "./data"  ]; then
  mkdir data
fi
for file in ./data/*
do
  echo Analizing $file
  python3 window_size_analizer.py $file >> ./recolected_info/window_sizes.data
done

if [ ! -d "./recolected_info"  ]; then
  mkdir recolected_info
fi
if [ ! -d "./data"  ]; then
  mkdir data
fi
for file in ./data/*
do
  echo Analizing $file
  python3 time_window_analizer.py $file >> ./recolected_info/time_window.data
done

import numpy as np 

# Variable Instantiation
aqi_list = [18.0, 9.0, 20.0, 11.0, 6.0, 11.0, 7.0, 3.0, 7.0, 13.0, 18.0, 5.0, 35.0, 18.0, 23.0, 0.0, 11.0, 9.0, 15.0, 13.0, 19.0, 10.0, 20.0, 32.0, 8.0, 6.0, 13.0, 13.0, 5.0, 33.0, 13.0, 19.0, 16.0, 10.0, 41.0, 17.0, 11.0, 6.0, 13.0, 24.0, 13.0, 28.0, 10.0, 17.0, 14.0, 31.0, 28.0, 7.0, 13.0, 38.0, 22.0, 19.0, 18.0, 20.0, 39.0, 15.0, 17.0, 55.0, 22.0, 35.0, 10.0, 56.0, 30.0, 30.0, 11.0, 18.0, 11.0, 22.0, 11.0, 24.0, 11.0, 7.0, 11.0, 11.0, 0.0, 28.0, 9.0, 9.0, 6.0, 26.0, 27.0, 14.0, 16.0, 5.0, 9.0, 24.0, 17.0, 16.0, 6.0, 3.0, 14.0, 52.0, 8.0, 7.0, 17.0, 14.0, 18.0, 6.0, 19.0, 11.0, 13.0, 7.0, 13.0, 16.0, 6.0, 5.0, 10.0, 74.0, 6.0, 2.0, 22.0, 19.0, 15.0, 13.0, 8.0, 44.0, 76.0, 32.0, 2.0, 22.0, 35.0, 18.0, 23.0, 66.0, 14.0, 60.0, 20.0, 36.0, 9.0, 19.0, 23.0, 33.0, 10.0, 16.0, 13.0, 47.0, 0.0, 6.0, 11.0, 25.0, 7.0, 10.0, 8.0, 22.0, 17.0, 24.0, 15.0, 13.0, 8.0, 16.0, 9.0, 15.0, 23.0, 31.0, 20.0, 28.0, 13.0, 26.0, 11.0, 13.0, 7.0, 9.0, 11.0, 19.0, 16.0, 18.0, 5.0, 13.0, 9.0, 47.0, 31.0, 42.0, 15.0, 58.0, 57.0, 14.0, 9.0, 35.0, 28.0, 45.0, 8.0, 18.0, 16.0, 30.0, 5.0, 11.0, 15.0, 16.0, 5.0, 0.0, 13.0, 40.0, 10.0, 3.0, 15.0, 28.0, 5.0, 6.0, 24.0, 5.0, 13.0, 16.0, 43.0, 5.0, 7.0, 14.0, 18.0, 15.0, 8.0, 3.0, 19.0, 6.0, 6.0, 32.0, 13.0, 32.0, 20.0, 16.0, 48.0, 18.0, 23.0, 36.0, 31.0, 11.0, 2.0, 51.0, 32.0, 5.0, 11.0, 27.0, 7.0, 34.0, 18.0, 25.0, 7.0, 18.0, 14.0, 20.0, 23.0, 16.0, 6.0, 8.0, 5.0, 13.0, 11.0, 5.0, 11.0, 14.0, 8.0, 6.0, 35.0, 38.0, 22.0, 93.0, 10.0, 11.0, 6.0, 43.0, 5.0, 16.0, 7.0, 13.0, 10.0, 7.0, 11.0, 31.0, 23.0, 9.0, 20.0, 24.0, 8.0, 11.0, 18.0, 15.0, 17.0, 9.0, 18.0, 7.0, 7.0, 7.0, 9.0, 17.0, 9.0, 15.0, 7.0, 6.0, 19.0, 8.0, 23.0, 45.0, 18.0, 17.0, 54.0, 10.0, 16.0, 39.0, 6.0, 8.0, 17.0, 14.0, 14.0, 13.0, 18.0, 9.0, 9.0, 22.0, 11.0, 9.0, 39.0, 40.0, 30.0, 11.0, 16.0, 10.0, 9.0, 38.0, 16.0, 47.0, 9.0, 6.0, 5.0, 33.0, 18.0, 17.0, 24.0, 8.0, 7.0, 1.0, 10.0, 16.0, 6.0, 6.0, 20.0, 6.0, 28.0, 8.0, 19.0, 19.0, 36.0, 24.0, 5.0, 20.0, 10.0, 7.0, 15.0, 8.0, 6.0, 7.0, 15.0, 25.0, 6.0, 19.0, 40.0, 19.0, 9.0, 20.0, 14.0, 0.0, 7.0, 6.0, 13.0, 22.0, 8.0, 9.0, 50.0, 8.0, 13.0, 11.0, 8.0, 30.0, 11.0, 6.0, 5.0, 10.0, 6.0, 6.0, 30.0, 9.0, 13.0, 13.0, 8.0, 7.0, 23.0, 6.0, 18.0, 9.0, 34.0, 5.0, 3.0, 6.0, 11.0, 45.0, 35.0, 32.0, 2.0, 7.0, 13.0, 0.0, 30.0, 23.0, 8.0, 20.0, 6.0, 47.0, 3.0, 10.0, 7.0, 5.0, 2.0, 10.0, 8.0, 3.0, 5.0, 10.0, 16.0, 22.0, 13.0, 15.0, 10.0, 20.0, 36.0, 11.0, 10.0, 11.0, 17.0, 14.0, 1.0, 16.0, 17.0, 32.0, 49.0, 2.0, 15.0, 32.0, 25.0, 49.0, 6.0, 23.0, 19.0, 19.0, 32.0, 13.0, 20.0, 10.0, 16.0, 14.0, 24.0, 40.0, 15.0, 9.0, 11.0, 15.0, 11.0, 13.0, 40.0, 49.0, 8.0, 8.0, 25.0, 13.0, 40.0, 19.0, 16.0, 3.0, 14.0, 23.0, 22.0, 11.0, 15.0, 3.0, 13.0, 15.0, 59.0, 16.0, 20.0, 5.0, 24.0, 6.0, 16.0, 16.0, 2.0, 5.0, 17.0, 25.0, 28.0, 16.0, 13.0, 15.0, 2.0, 13.0, 9.0, 11.0, 10.0, 11.0, 11.0, 11.0, 6.0, 10.0, 6.0, 6.0, 19.0, 11.0, 13.0, 6.0, 9.0, 9.0, 10.0, 36.0, 8.0, 6.0, 7.0, 8.0, 30.0, 24.0, 23.0, 15.0, 6.0, 1.0, 2.0, 0.0, 1.0, 24.0, 28.0, 9.0, 9.0, 11.0, 10.0, 15.0, 15.0, 6.0, 0.0, 15.0, 15.0, 13.0, 5.0, 13.0, 10.0, 18.0, 36.0, 39.0, 7.0, 31.0, 5.0, 11.0, 23.0, 13.0, 20.0, 8.0, 17.0, 7.0, 30.0, 11.0, 20.0, 11.0, 17.0, 17.0, 10.0, 2.0, 19.0, 11.0, 18.0, 7.0, 24.0, 24.0, 10.0, 11.0, 8.0, 15.0, 28.0, 3.0, 16.0, 28.0, 14.0, 7.0, 35.0, 10.0, 26.0, 5.0, 1.0, 13.0, 5.0, 16.0, 18.0, 11.0, 16.0, 13.0, 34.0, 5.0, 0.0, 11.0, 10.0, 15.0, 14.0, 6.0, 10.0, 15.0, 25.0, 3.0, 9.0, 20.0, 2.0, 3.0, 17.0, 14.0, 34.0, 5.0, 18.0, 66.0, 22.0, 25.0, 6.0, 14.0, 28.0, 16.0, 10.0, 47.0, 14.0, 39.0, 2.0, 2.0, 36.0, 14.0, 6.0, 16.0, 14.0, 5.0, 28.0, 8.0, 11.0, 39.0, 11.0, 14.0, 17.0, 3.0, 1.0, 6.0, 7.0, 5.0, 3.0, 9.0, 8.0, 7.0, 2.0, 8.0, 14.0, 8.0, 0.0, 15.0, 13.0, 19.0, 20.0, 30.0, 9.0, 6.0, 10.0, 7.0, 13.0, 13.0, 5.0, 3.0, 9.0, 3.0, 14.0, 2.0, 1.0, 0.0, 1.0, 1.0, 8.0, 3.0, 23.0, 13.0, 7.0, 6.0, 18.0, 7.0, 3.0, 14.0, 25.0, 11.0, 2.0, 17.0, 17.0, 6.0, 19.0, 18.0, 22.0, 6.0, 8.0, 1.0, 13.0, 9.0, 17.0, 5.0, 7.0, 8.0, 6.0, 10.0, 5.0, 5.0, 2.0, 10.0, 18.0, 13.0, 26.0, 11.0, 3.0, 7.0, 22.0, 7.0, 24.0, 11.0, 18.0, 0.0, 9.0, 7.0, 8.0, 9.0, 3.0, 11.0, 5.0, 6.0, 9.0, 11.0, 18.0, 0.0, 0.0, 18.0, 6.0, 24.0, 24.0, 5.0, 2.0, 6.0, 11.0, 15.0, 14.0, 7.0, 18.0, 15.0, 6.0, 24.0, 15.0, 5.0, 9.0, 8.0, 8.0, 1.0, 7.0, 2.0, 8.0, 3.0, 3.0, 6.0, 15.0, 14.0, 36.0, 11.0, 7.0, 11.0, 15.0, 24.0, 26.0, 14.0, 16.0, 18.0, 7.0, 3.0, 7.0, 7.0, 3.0, 10.0, 33.0, 6.0, 45.0, 9.0, 14.0, 17.0, 5.0, 5.0, 3.0, 5.0, 19.0, 8.0, 28.0, 8.0, 13.0, 61.0, 9.0, 16.0, 14.0, 8.0, 7.0, 16.0, 3.0, 3.0, 32.0, 10.0, 17.0, 16.0, 10.0, 3.0, 1.0, 23.0, 20.0, 50.0, 34.0, 7.0, 9.0, 14.0, 17.0, 13.0, 3.0, 18.0, 1.0, 7.0, 10.0, 17.0, 11.0, 8.0, 3.0, 10.0, 7.0, 6.0, 7.0, 16.0, 5.0, 18.0, 16.0, 8.0, 13.0, 6.0, 9.0, 38.0, 25.0, 7.0, 10.0, 15.0, 6.0, 7.0, 5.0, 3.0, 11.0, 10.0, 5.0, 14.0, 8.0, 32.0, 7.0, 17.0, 24.0, 19.0, 7.0, 20.0, 8.0, 3.0, 2.0, 2.0, 24.0, 14.0, 16.0, 6.0, 11.0, 10.0, 32.0, 6.0, 5.0, 3.0, 5.0, 9.0, 3.0, 18.0, 11.0, 8.0, 8.0, 6.0, 14.0, 9.0, 5.0, 10.0, 10.0, 5.0, 6.0, 3.0, 8.0, 7.0, 0.0, 22.0, 19.0, 33.0, 22.0, 1.0, 15.0, 8.0, 9.0, 10.0, 13.0, 10.0, 1.0, 2.0, 24.0, 6.0, 8.0, 24.0, 1.0, 11.0, 7.0, 7.0, 1.0, 6.0, 6.0, 8.0, 6.0, 10.0, 5.0, 10.0, 9.0, 17.0, 34.0, 16.0, 7.0, 5.0, 15.0, 5.0, 17.0, 5.0, 5.0, 5.0, 11.0, 6.0, 10.0, 3.0, 6.0, 9.0, 6.0, 17.0, 9.0, 3.0, 5.0, 6.0, 5.0, 5.0, 31.0, 2.0, 20.0, 9.0, 9.0, 8.0, 10.0, 9.0, 18.0, 9.0, 7.0, 2.0, 8.0, 24.0, 7.0, 13.0, 16.0, 26.0, 25.0, 3.0, 3.0, 8.0, 2.0, 9.0, 7.0, 7.0, 2.0, 17.0, 2.0, 3.0, 5.0, 6.0, 13.0, 11.0, 16.0, 3.0, 17.0, 19.0, 60.0, 28.0, 0.0, 0.0, 25.0, 8.0, 8.0, 11.0, 22.0, 3.0, 26.0, 0.0, 5.0, 3.0, 3.0, 7.0, 7.0, 9.0, 10.0, 3.0, 14.0, 11.0, 7.0, 15.0, 24.0, 13.0, 8.0, 1.0, 8.0, 8.0, 8.0, 3.0, 16.0, 17.0, 5.0, 8.0, 5.0, 10.0, 7.0, 8.0, 3.0, 8.0, 14.0, 5.0, 9.0, 10.0, 8.0, 6.0, 3.0, 13.0, 8.0, 15.0, 11.0, 9.0, 22.0, 13.0, 5.0, 6.0, 7.0, 9.0, 7.0, 14.0, 6.0, 7.0, 22.0, 16.0, 7.0, 18.0, 8.0, 10.0, 6.0, 7.0, 19.0, 7.0, 5.0, 10.0, 6.0, 9.0, 2.0, 6.0, 6.0, 7.0, 0.0, 3.0, 15.0, 2.0, 13.0, 30.0, 0.0, 6.0, 5.0, 7.0, 9.0, 7.0, 10.0, 14.0, 13.0, 10.0, 10.0, 6.0, 8.0, 14.0, 5.0, 15.0, 0.0, 17.0, 2.0, 8.0, 14.0, 7.0, 16.0, 8.0, 7.0, 28.0, 14.0, 25.0, 5.0, 6.0, 5.0, 6.0, 6.0, 5.0, 10.0, 3.0, 3.0, 10.0, 13.0, 5.0, 8.0, 2.0, 8.0, 23.0, 9.0, 3.0, 9.0, 2.0, 3.0, 5.0, 9.0, 2.0, 1.0, 2.0, 5.0, 2.0, 8.0, 7.0, 2.0, 0.0, 8.0, 2.0, 8.0, 22.0, 11.0, 7.0, 5.0, 8.0, 2.0, 5.0, 3.0, 6.0, 7.0, 7.0, 6.0, 17.0, 2.0, 2.0, 8.0, 5.0, 3.0, 5.0, 3.0, 7.0, 8.0, 6.0, 3.0, 15.0, 8.0, 10.0, 3.0, 8.0, 15.0, 5.0, 8.0, 19.0, 5.0, 7.0, 6.0, 8.0, 5.0, 2.0, 8.0, 10.0, 8.0, 0.0, 10.0, 27.0, 2.0, 6.0, 3.0, 11.0, 5.0, 3.0, 1.0, 1.0, 3.0, 14.0, 8.0, 5.0, 11.0, 7.0, 2.0, 0.0, 6.0, 2.0, 5.0, 6.0, 5.0, 6.0, 6.0, 5.0, 5.0, 8.0, 2.0, 11.0, 8.0, 7.0, 3.0, 0.0, 8.0, 5.0, 6.0, 1.0, 7.0, 6.0, 3.0, 13.0, 13.0, 8.0, 2.0, 0.0, 10.0, 7.0, 6.0, 3.0, 8.0, 3.0, 3.0, 6.0, 3.0, 6.0, 9.0, 7.0, 3.0, 5.0, 6.0, 3.0, 8.0, 3.0, 3.0, 9.0, 2.0, 2.0, 10.0, 2.0, 3.0, 5.0, 10.0, 7.0, 5.0, 5.0, 3.0, 0.0, 2.0, 20.0, 16.0, 7.0, 2.0, 6.0, 10.0, 3.0, 3.0, 0.0, 3.0, 7.0, 5.0, 2.0, 5.0, 8.0, 7.0, 17.0, 28.0, 6.0, 2.0, 8.0, 10.0, 9.0, 0.0, 13.0, 5.0, 5.0, 6.0, 17.0, 13.0, 8.0, 5.0, 11.0, 7.0, 3.0, 10.0, 22.0, 13.0, 3.0, 11.0, 7.0, 14.0, 9.0, 9.0, 2.0, 3.0, 6.0, 1.0, 10.0, 9.0, 7.0, 16.0, 13.0, 2.0, 11.0, 7.0, 3.0, 6.0, 13.0, 6.0, 3.0, 14.0, 0.0, 0.0, 3.0, 7.0, 5.0, 16.0, 13.0, 8.0, 10.0, 79.0, 18.0, 10.0, 7.0, 23.0, 8.0, 6.0, 5.0, 3.0, 0.0, 6.0, 10.0, 15.0, 2.0, 8.0, 2.0, 3.0, 7.0, 3.0, 2.0, 13.0, 9.0, 6.0, 6.0, 2.0, 8.0, 13.0, 2.0, 13.0, 0.0, 5.0, 11.0, 6.0, 3.0, 6.0, 0.0, 3.0, 2.0, 5.0, 11.0, 6.0, 3.0, 3.0, 7.0, 6.0, 2.0, 22.0, 1.0, 6.0, 2.0, 6.0, 5.0, 7.0, 2.0, 5.0, 23.0, 23.0, 2.0, 10.0, 5.0, 5.0, 11.0, 3.0, 1.0, 2.0, 5.0, 5.0, 2.0, 2.0, 6.0, 1.0, 5.0, 2.0, 6.0, 8.0, 9.0, 6.0, 1.0, 5.0, 11.0, 6.0, 8.0, 2.0, 2.0, 2.0, 5.0, 3.0, 8.0, 3.0, 2.0, 5.0, 1.0, 3.0, 2.0, 2.0, 6.0, 5.0, 3.0, 3.0, 7.0, 6.0, 6.0, 1.0, 3.0, 3.0, 10.0, 6.0, 16.0, 16.0, 5.0, 0.0, 2.0, 1.0, 20.0, 5.0, 2.0, 2.0, 3.0, 5.0, 5.0, 6.0, 7.0, 6.0, 7.0, 3.0, 3.0, 2.0, 5.0, 6.0, 3.0, 7.0, 7.0, 2.0, 3.0, 2.0, 2.0, 8.0, 9.0, 5.0, 5.0, 1.0, 2.0, 6.0, 2.0, 3.0, 3.0, 5.0, 5.0, 6.0, 3.0, 1.0, 3.0, 3.0, 8.0, 3.0, 2.0, 1.0, 2.0, 3.0, 1.0, 2.0, 6.0, 2.0, 3.0, 6.0, 2.0, 2.0, 2.0, 5.0, 13.0, 9.0, 1.0, 6.0, 7.0, 2.0, 8.0, 2.0, 3.0, 8.0, 3.0, 6.0, 3.0, 5.0, 8.0, 2.0, 8.0, 2.0, 9.0, 2.0, 2.0, 5.0, 6.0, 5.0, 6.0, 2.0, 6.0, 3.0, 2.0, 8.0, 3.0, 3.0, 1.0, 1.0, 3.0, 2.0, 3.0, 1.0, 2.0, 15.0, 7.0, 2.0, 2.0, 5.0, 2.0, 3.0, 5.0, 3.0, 5.0, 2.0, 5.0, 3.0, 6.0, 6.0, 5.0, 5.0, 2.0, 5.0, 2.0, 10.0, 3.0, 7.0, 5.0, 3.0, 1.0, 5.0, 2.0, 8.0, 6.0, 3.0, 6.0, 0.0, 3.0, 2.0, 5.0, 5.0, 3.0, 5.0, 5.0, 6.0, 5.0, 6.0, 5.0, 14.0, 5.0, 5.0, 7.0, 2.0, 5.0, 1.0, 0.0, 3.0, 6.0, 5.0, 9.0, 8.0, 9.0, 2.0, 6.0, 5.0, 3.0, 13.0, 7.0, 5.0, 2.0, 2.0, 5.0, 2.0, 2.0, 6.0, 7.0, 2.0, 3.0, 5.0, 5.0, 5.0, 6.0, 9.0, 2.0, 9.0, 1.0, 5.0, 7.0, 5.0, 6.0, 1.0, 7.0, 9.0, 1.0, 5.0, 0.0, 7.0, 1.0, 3.0, 6.0, 2.0, 3.0, 0.0, 7.0, 3.0, 3.0, 3.0, 3.0, 7.0, 3.0, 5.0, 5.0, 8.0, 2.0, 13.0, 17.0, 11.0, 2.0, 3.0, 6.0, 3.0, 0.0, 5.0, 1.0, 2.0, 5.0, 3.0, 2.0, 0.0, 5.0, 5.0, 7.0, 9.0, 2.0, 2.0, 2.0, 1.0, 5.0, 6.0, 3.0, 7.0, 5.0, 6.0, 14.0, 3.0, 1.0, 2.0, 1.0, 5.0, 1.0, 5.0, 3.0, 3.0, 6.0, 2.0, 5.0, 6.0, 5.0, 2.0, 5.0, 9.0, 3.0, 9.0, 2.0, 3.0, 2.0, 3.0, 5.0, 1.0, 7.0, 8.0, 1.0, 5.0, 10.0, 2.0, 3.0, 3.0, 10.0, 3.0, 2.0, 3.0, 5.0, 10.0, 6.0, 3.0, 3.0, 3.0, 5.0, 2.0, 3.0, 6.0, 5.0, 2.0, 7.0, 5.0, 3.0, 0.0]

## Task 1: Create array using numpy

# convert list to array using numpy function
aqi_array = np.array(aqi_list)

# print len of array
#print(len(aqi_array))

# print first 5 elements
#print(aqi[:5]) || aqi[:5] || a for loop

## Task 2: Calculate summary statistics

# Get maximum value
print(f"Max: {np.max(aqi_array)}")                 #aqi_array.max() also works

# Get Minimum value
print(f"Min: {np.min(aqi_array)}")                 #aqi_array.min() also works

# Get Median value
print(f"Median: {np.median(aqi_array)}")           #aqi_array.median() does NOT work

# Get Standard Deviation
print(f"Standard Deviation: {np.std(aqi_array)}")  #aqi_array.std() also works

## Task 3: Calculate percentage of readings with cleanest AQI ##
## readings of 5 or less

# Find all entries of aqi_array that are less than or equal to 5 and add returned boolean values to new boolean_array
boolean_aqi = aqi_array <= 5

# Calculate number of True values and divide by total number of values in boolean_array
percent_under_6 = np.mean(boolean_aqi)   # same as percent_under_6 = boolean_aqi.sum() / len(boolean_aqi)

    # This works because np.mean(boolean_aqi) calculates the mean of the boolean array, treating True as 1 and False as 0. 
    # Since array contains only True and False values, this effectively calculates the percentage of Truevalues in the array.
    # Result of np.mean(boolean_aqi) is the sum of all values (where True = 1 and False = 0) divided by the total number of values in the array.
                                                                               
print("Percentage of True values:", percent_under_6)


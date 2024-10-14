scrape('https://weather.com/weather/today/l/44.92,-92.87?par=google&temp=f')
l = soup.find(title="Weather Today in Woodbury, MN")
k = l.find(class_="_-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2icPt")
feelslike = k.text
k = l.find(class_="_-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL")
j = k.find(class_="_-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q")
high_low = j.text
print("Today's Weather Forecast: \n\nIt feels like %s right now and today's high and low temperatures are %s." % (feelslike, high_low))

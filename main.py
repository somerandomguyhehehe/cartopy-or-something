import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# 1. Ask the user for input (accepts names like 'red' or hex codes like '#FF5733')
chosen_color = input("Enter marker color name or hex code")

# 2. Build the plot
plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

# Sample point (Paris)
lon, lat = 2.3522, 48.8566

# 3. Pass user selection to the color parameter
ax.plot(lon, lat, 
        marker='o', 
        color=chosen_color, 
        markersize=12, 
        transform=ccrs.PlateCarree())

plt.show()
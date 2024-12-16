
# Set NEW NASA wallpaper

Sets a new NASA wallpaper daily fetched from NASA's APOD API image.

How it works?

A cronjob runs once everyday on system reboot.

Then the script run_once_daily.sh checks if set_wallpaper_on_login.sh has already run by creating a timestamp file and comparing the current date to it.

If the script has run once for the day then the script exits.

Else set_wallpaper_on_login.sh gets executed which activates the virtual environment.

Then Python script executes ,loads .env file,checks for internet connection for 15 minutes and if found fetches and sets image fetched from API as wallpaper else exits.




## API Reference

#### Get all items

```http
  GET https://api.nasa.gov/planetary/apod?api_key={api_key}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

data = res.json()
image_url = data.get('url') 
fetches the image url




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY` of NASA open API

`


## Run Locally

Clone the project

```bash
  git clone https://github.com/Risriddle/DailyNASAWallpaper.git
```

Go to the project directory

```bash
  cd DailyNASAWallpaper
```


Create virtual environment and actvate it

```bash
  python3 venv -m <envName>
  source venv/bin/activate
```

Install dependencies

```bash
  pip3 install requirements.txt
```

Replace system folder names in scripts and create .env file for API key

Create cronjob

```bash
  crontab -e
  @reboot /home/username/DailyNASAWallpaper/run_once_daily.sh
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

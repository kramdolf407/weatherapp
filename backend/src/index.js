const debug = require('debug')('weathermap');

const Koa = require('koa');
const router = require('koa-router')();
const fetch = require('node-fetch');
const cors = require('kcors');

const appId = process.env.APPID || '';
const mapURI = process.env.MAP_ENDPOINT || "http://api.openweathermap.org/data/2.5";
const targetCity = process.env.TARGET_CITY || "Stockholm,se";
const whitelist = ["http://backend:9000/api/weather", "http://frontend:8000"];

const port = process.env.PORT || 9000;

const app = new Koa();

function checkOriginAgainstWhitelist(ctx) {
  const requestOrigin = ctx.accept.headers.origin;
  if (!whitelist.includes(requestOrigin) ){
    return ctx.throw(`🙈 ${requestOrigin} is not a valid origin`);
  }
  return requestOrigin;
}

app.use(cors({ origin: checkOriginAgainstWhitelist }));

/*app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});*/

const fetchWeather = async () => {
  const endpoint = `${mapURI}/weather?q=${targetCity}&appid=${appId}&`;
  const response = await fetch(endpoint);

  return response ? response.json() : {}
};

router.get('/api/weather', async ctx => {
  const weatherData = await fetchWeather();
  console.log("Was a connection requested by frontend? :) ");
  //ctx.response.cors.
  ctx.type = 'application/json; charset=utf-8';
  ctx.body = weatherData.weather ? weatherData.weather[0] : {};
});


app.use(router.routes());
app.use(router.allowedMethods());



app.listen(port);

console.log(`App listening on port ${port}`);

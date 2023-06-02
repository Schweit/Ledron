  import time
  from rpi_ws281x import Color, PixelStrip, ws

  # LED strip configuration:
  LED_COUNT = 170        # Number of LED pixels.
  LED_PIN = 18           # GPIO pin connected to the pixels (must support PWM!).
  LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
  LED_DMA = 10           # DMA channel to use for generating signal (try 10)
  LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
  LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
  LED_CHANNEL = 0
  LED_STRIP = ws.SK6812_STRIP_RGBW
  # LED_STRIP = ws.SK6812W_STRIP

  def colorWipe(strip, color, wait_ms=50):
  for i in range(strip.numPixels()):
      strip.setPixelColor(i, color)
      strip.show()
      time.sleep(wait_ms / 1000.0)

  strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

  strip.begin()
  while True:
       colorWipe(strip, Color(255, 12, 0, 25))

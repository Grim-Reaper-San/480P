#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='''ffmpeg -i "{}" -filter_complex "[0:v]drawtext=fontfile=font.ttf:text='t.me/animext':fontsize=16:fontcolor=ffffff:alpha='if(lt(t,0),0,if(lt(t,5),(t-0)/5,if(lt(t,15),1,if(lt(t,20),(5-(t-15))/5,0))))':x=w-text_w-15:y=15" -pix_fmt yuv420p10le -s 854x480 -preset medium -c:v libx265 -crf 24.9 -map 0:v -c:a libopus -b:a 72k -map 0:a -c:s copy -map 0:s? "{}"''',
    )
    THUMB = config(
        "THUMBNAIL", default="www.google.com"
    )
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)

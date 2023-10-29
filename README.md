# Masonite Ambient

This project is an ambient sound mixer. This mixer contains rain, thunder and campfire sounds all the way to parrots, whales and dinosaurs.

create your own landscape effects to help you focus.

## Installation

```
$ npm install
$ npm run dev
$ python craft serve
```

## Adding your own sounds

Adding your own sounds are simple.

1. find a sound mp3. the audio file will automatically loop so find the best sound loop. you can find sounds on free sound websites.

2. add the sound to the `/public` directory. again it should be a short mp3. usually around 30 seconds.

3. We need a logo. all logos must be svg files. the toggle icons should be an svg with the naming schema of `imageName.svg` and when the sound s off it is `imageName-noplay.svg` for "not playing".

4. finally add the sound to the `welcome.html` page using the vue `SoundComponent`.

```html
<sound-component file="public/train.mp3" icon="/images/train" label="train"></sound-component>
```

## Playlists

playlists are sound mixes that save a collection of sounds and their volumes. to create a playlist go to the `PlaylistComponent` and add a component with a name to the top of the template

```html
        <div class="px-8 m-2 w-1/4 border-2 cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-2 border-gray-300" @click="play('New Playlist Name')"> New Playlist Name </div>
```

then near the bottom of the file add that name to the array of playlists with your desired sounds.

```javascript
'New Playlist Name': [
    {"label": "car-rain", "volume": 100},
    {"label": "train", "volume": 100},
    {"label": "thunder", "volume": 1},
    {"label": "night", "volume": 30},
]
```

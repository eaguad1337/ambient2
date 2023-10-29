<style scoped>
.isActive {
    background-color: #4299e1;
    color: #fff;
}
</style>

<template>
    <div class="grid grid-cols-1 md:grid-cols-6 gap-5">
        <div :class="{ isActive: playlistIsActive('Camping') }" class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="play('Camping')"> Camping </div>
        <div :class="{ isActive: playlistIsActive('Calm in a car') }" class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="play('Calm in a car')"> Calm in a car </div>
        <div :class="{ isActive: playlistIsActive('Driving at night in the rain') }" class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="play('Driving at night in the rain')"> Driving at night in the rain </div>
        <div :class="{ isActive: playlistIsActive('Thunder Train') }" class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="play('Thunder Train')"> Thunder Train</div>
        <div :class="{ isActive: playlistIsActive('Summer Day') }" class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="play('Summer Day')"> Summer Day </div>
        <div :class="{ isActive: playlistIsActive('Sleeping by the beach') }" class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="play('Sleeping by the beach')"> Sleeping by the beach </div>
        <div :class="{ isActive: playlistIsActive('Cafe') }" class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="play('Cafe')"> Cafe </div>
        <div :class="{ isActive: playlistIsActive('City') }" class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="play('City')"> City </div>
        <div :class="{ isActive: playlistIsActive('Rainy Traffic') }" class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="play('Rainy Traffic')"> Rainy Traffic </div>
        <div class="px-8 flex items-center justify-center cursor-pointer hover:bg-blue-200 py-6 text-center shadow-xl border-rounded bg-gray-100 border-gray-300" @click="mute()">
            <img src="/images/mute.svg" style="width: 35px"/>
        </div>
    </div>
</template>

<script>
import { EventBus } from '../app.js';
export default {
    data() {
        return {
            'selectedPlaylist': null,
            'playlists': {
                'Camping': [
                    {"label": "fire", "volume": 20},
                    {"label": "rain", "volume": 60},
                    {"label": "night", "volume": 60},
                    {"label": "thunder", "volume": 40},
                    {"label": "cicada", "volume": 5},
                    {"label": "frog", "volume": 15},
                ],
                'Thunder Train': [
                    {"label": "car-rain", "volume": 100},
                    {"label": "rain", "volume": 60},
                    {"label": "thunder", "volume": 100},
                    {"label": "train", "volume": 100},
                    {"label": "heartbeat", "volume": 100},
                    {"label": "cafe", "volume": 60},
                ],
                'Calm in a car': [
                    {"label": "rain", "volume": 30},
                    {"label": "car-rain", "volume": 100},
                    {"label": "thunder", "volume": 70},
                    {"label": "cicada", "volume": 5},
                    {"label": "night", "volume": 45},
                ],
                'Driving at night in the rain': [
                    {"label": "car-rain", "volume": 100},
                    {"label": "train", "volume": 100},
                    {"label": "thunder", "volume": 1},
                    {"label": "night", "volume": 30},
                ],
                'Rainy Traffic': [
                    {"label": "car-rain", "volume": 100},
                    {"label": "car", "volume": 60},
                    {"label": "thunder", "volume": 100},
                    {"label": "city", "volume": 25},
                ],
                'Summer Day': [
                    {"label": "air-conditioner", "volume": 100},
                    {"label": "lawnmower", "volume": 30},
                    {"label": "bird", "volume": 50},
                ],
                'Sleeping by the beach': [
                    {"label": "cicada", "volume": 5},
                    {"label": "ocean", "volume": 60},
                    {"label": "night", "volume": 100},
                    {"label": "fire", "volume": 100},
                    {"label": "car", "volume": 10},
                    {"label": "heartbeat", "volume": 100},
                    {"label": "blaze", "volume": 20},
                ],
                'Train Ride': [
                    {"label": "train", "volume": 100},
                    {"label": "heartbeat", "volume": 100},
                    {"label": "air-conditioner", "volume": 100},
                ],
                'Cafe': [
                    {"label": "cafe", "volume": 30},
                    {"label": "jazz", "volume": 30},
                    {"label": "bird", "volume": 20},
                    {"label": "car", "volume": 15},
                    {"label": "record", "volume": 10},
                    {"label": "fire", "volume": 50},
                ],
                'City': [
                    {"label": "city", "volume": 25},
                    {"label": "construction", "volume": 25},
                    {"label": "car", "volume": 25},
                ],
            }
        }
    },
    methods: {
        playlistIsActive(playlist) {
            return this.selectedPlaylist == playlist
        },
        play(playlist){
            this.mute()
            this.selectedPlaylist = playlist

            let sound;
            for (sound of this.playlists[playlist]) {
                console.log(sound)
                EventBus.$emit(`play-${sound.label}-volume`, sound.volume)
            }
        },
        mute(playlist) {
            this.selectedPlaylist = null
            EventBus.$emit("adjust-volume", 0)
        }
    }
}
</script>
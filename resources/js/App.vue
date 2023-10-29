<template>
    <div class="mx-auto container flex flex-col justify-center">
        <header-component></header-component>
        <h2 class="my-10 font-bold text-2xl">
            Select a preset
        </h2>

        <playlist-component></playlist-component>

        <h2 class="my-10 font-bold text-2xl">
            Customize your experience
        </h2>

        <div class="my-10 grid grid-cols-1 md:grid-cols-4 gap-5">
            <sound-component file="public/rain.mp3" icon="/images/rain" label="rain"></sound-component>
            <sound-component file="public/fire.mp3" icon="/images/campfire" label="fire"></sound-component>
            <sound-component file="public/cicada.mp3" icon="/images/cicada" label="cicada"></sound-component>
            <sound-component file="public/wind.mp3" icon="/images/wind" label="wind"></sound-component>
            <sound-component file="public/leaf.mp3" icon="/images/leaf" label="leaf"></sound-component>
            <sound-component file="public/boat.mp3" icon="/images/boat" label="boat"></sound-component>
            <sound-component file="public/plane.mp3" icon="/images/plane" label="plane"></sound-component>
            <sound-component file="public/parrot.mp3" icon="/images/parrot" label="parrot"></sound-component>
            <sound-component file="public/night.mp3" icon="/images/night" label="night"></sound-component>
            <sound-component file="public/ocean.mp3" icon="/images/ocean" label="ocean"></sound-component>
            <sound-component file="public/thunder.mp3" icon="/images/thunder" label="thunder"></sound-component>
            <sound-component file="public/car-rain.mp3" icon="/images/car-rain" label="car-rain"></sound-component>
            <sound-component file="public/farm.mp3" icon="/images/farm" label="farm"></sound-component>
            <sound-component file="public/car.mp3" icon="/images/car" label="car"></sound-component>
            <sound-component file="public/bird.mp3" icon="/images/bird" label="bird"></sound-component>
            <sound-component file="public/lawnmower.mp3" icon="/images/lawnmower" label="lawnmower"></sound-component>
            <sound-component file="public/air-conditioner.mp3" icon="/images/air-conditioner" label="air-conditioner"></sound-component>
            <sound-component file="public/blaze.mp3" icon="/images/blaze" label="blaze"></sound-component>
            <sound-component file="public/heartbeat.mp3" icon="/images/heartbeat" label="heartbeat"></sound-component>
            <sound-component file="public/train.mp3" icon="/images/train" label="train"></sound-component>
            <sound-component file="public/jazz.mp3" icon="/images/jazz" label="jazz"></sound-component>
            <sound-component file="public/cafe.mp3" icon="/images/cafe" label="cafe"></sound-component>
            <sound-component file="public/construction.mp3" icon="/images/construction" label="construction"></sound-component>
            <sound-component file="public/frog.mp3" icon="/images/frog" label="frog"></sound-component>
            <sound-component file="public/record.mp3" icon="/images/record" label="record"></sound-component>
            <sound-component file="public/city.mp3" icon="/images/city" label="city"></sound-component>
            <sound-component file="public/whale.mp3" icon="/images/whale" label="whale"></sound-component>
            <sound-component file="public/dinosaur.mp3" icon="/images/dinosaur" label="dinosaur"></sound-component>
        </div>
    </div>
</template>

<script>
import PlaylistComponent from "./components/PlaylistComponent.vue"
import SoundComponent from "./components/SoundComponent.vue"
import HeaderComponent from "./components/HeaderComponent.vue"

export default {
    components: {
        HeaderComponent,
        PlaylistComponent,
        SoundComponent
    }
}
</script>


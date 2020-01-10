<template>
    <div class="sister-gallery w-full">
        <div
            :key="queue"
            class="sister flex flex-col w-auto h-96 shadow-sister"
        >
            <div class="flex flex-row mt-8 self-center">
                <div>
                    <img
                        class="ml-8 w-56 h-40"
                        v-bind:src="slides[queue - 1].image"
                    />
                </div>
                <div class="mt-12 ml-12 leading-160 font-semibold text-lg w-96">
                    {{ slides[queue - 1].title }}
                </div>
            </div>
            <div class="mt-6 ml-10 mr-12 text-base text-grey leading-normal">
                {{ slides[queue - 1].description }}
            </div>
        </div>
        <div class="text-center">
            <span
                class="h-4 w-4 rounded-50 inline-block mt-16"
                v-bind:class="{
                    'bg-black': queue === 1,
                    'bg-carousel': queue !== 1
                }"
            />
            <span
                class="h-4 w-4 rounded-50 inline-block mt-16 ml-4"
                v-bind:class="{
                    'bg-black': queue === 2,
                    'bg-carousel': queue !== 2
                }"
            />
            <span
                class="h-4 w-4 rounded-50 inline-block mt-16 ml-4"
                v-bind:class="{
                    'bg-black': queue === 3,
                    'bg-carousel': queue !== 3
                }"
            />
        </div>
    </div>
</template>

<script>
import dsg from "@/assets/images/dsg.svg";
import pag from "@/assets/images/pag.svg";
import infosec from "@/assets/images/infosec.svg";
export default {
    name: "SisterGallery",
    data: function initData() {
        return {
            slides: [
                {
                    image: dsg,
                    title: "DATA SCIENCE GROUP",
                    description:
                        "As a part of SDS, this group aims at improving the culture of Data Science and Machine Learning in IIT Roorkee."
                },
                {
                    image: pag,
                    title: "PROGRAMMING & ALGORITHMS GROUP",
                    description:
                        "A bunch of competetive programming enthusiasts, PAG, frequently organizes coding lectures and contests for IITR people."
                },
                {
                    image: infosec,
                    title: "INFOSEC IITR",
                    description:
                        "InfoSecIITR is a group of information security enthusiasts. It is an open group that consists only of IITR students and alumni."
                }
            ],
            queue: 1
        };
    },
    methods: {
        swipedetect: function(el, callback) {
            var startX = 0;
            var touchsurface = el,
                swipedir,
                startY,
                distX,
                distY,
                threshold = 30,
                restraint = 300,
                allowedTime = 300,
                elapsedTime,
                startTime,
                handleswipe = callback || function(swipedir) {};

            touchsurface.addEventListener(
                "touchstart",
                function(e) {
                    var touchobj = e.changedTouches[0];
                    swipedir = "none";
                    startX = touchobj.pageX;
                    startY = touchobj.pageY;
                    startTime = new Date().getTime();
                    e.preventDefault();
                },
                false
            );

            touchsurface.addEventListener(
                "touchmove",
                function(e) {
                    e.preventDefault();
                },
                false
            );

            touchsurface.addEventListener(
                "touchend",
                function(e) {
                    var touchobj = e.changedTouches[0];
                    distX = touchobj.pageX - startX;
                    distY = touchobj.pageY - startY;
                    elapsedTime = new Date().getTime() - startTime;
                    if (
                        Math.abs(distX) >= threshold &&
                        Math.abs(distY) <= restraint
                    ) {
                        swipedir = distX < 0 ? "left" : "right";
                    } else if (
                        Math.abs(distY) >= threshold &&
                        Math.abs(distX) <= restraint
                    ) {
                        swipedir = distY < 0 ? "up" : "down";
                    }
                    handleswipe(swipedir);
                    e.preventDefault();
                },
                false
            );
        }
    },
    mounted() {
        var swipearea = document.getElementsByClassName("sister-gallery")[0];
        var vm = this;
        this.swipedetect(swipearea, function(swipedir) {
            if (swipedir == "left" || swipedir == "up") {
                if (vm.queue < 3) vm.queue++;
                else if (vm.queue == 3) vm.queue = 1;
            } else if (swipedir == "right" || swipedir == "down") {
                if (vm.queue > 1) vm.queue--;
                else if (vm.queue == 1) vm.queue = 3;
            }
        });
    }
};
</script>

<style lang="scss" scoped>
@keyframes slideIn {
    0% {
        transform: translate(100%, 0%);
        display: none;
        opacity: 1;
    }
    100% {
        transform: translate(0%, 0%);
        display: block;
        opacity: 1;
    }
}
.sister {
    animation: slideIn 1s ease forwards;
}
</style>

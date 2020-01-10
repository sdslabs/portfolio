<template>
    <div class="gallery flex flex-col w-auto sm:w-gallery">
        <img
            class="sm:h-128 sm:w-180 rounded-lg"
            v-bind:src="slides[queue - 1].image"
            alt="image"
        />
        <div
            class="textbox w-auto ml-6 mr-6 h-auto min-h-88 -mt-32 pr-6 sm:w-120 sm:h-auto sm:min-h-88 sm:ml-98 sm:-mt-gallery bg-white z-20"
        >
            <div class="font-extrabold text-2xl sm:text-lg mt-10 ml-10">
                {{ slides[queue - 1].title }}
            </div>
            <div
                class="sm:w-104 leading-170 text-grey text-xl sm:text-base mt-8 ml-10 mb-8"
            >
                {{ slides[queue - 1].description }}
            </div>
        </div>
        <div class="self-center sm:self-start sm:-mt-32">
            <span
                class="h-4 w-4 sm:h-3 sm:w-3 rounded-50 inline-block mt-16"
                v-bind:class="{
                    'bg-black': queue === 1,
                    'bg-carousel': queue !== 1
                }"
            />
            <span
                class="h-4 w-4 sm:h-3 sm:w-3 rounded-50 inline-block mt-16 ml-4"
                v-bind:class="{
                    'bg-black': queue === 2,
                    'bg-carousel': queue !== 2
                }"
            />
            <span
                class="h-4 w-4 sm:h-3 sm:w-3 rounded-50 inline-block mt-16 ml-4"
                v-bind:class="{
                    'bg-black': queue === 3,
                    'bg-carousel': queue !== 3
                }"
            />
            <span
                class="h-4 w-4 sm:h-3 sm:w-3 rounded-50 inline-block mt-16 ml-4"
                v-bind:class="{
                    'bg-black': queue === 4,
                    'bg-carousel': queue !== 4
                }"
            />
        </div>
    </div>
</template>

<script>
import lectures from "@/assets/images/lectures.png";
import hackathons from "@/assets/images/hackathons.png";
import workshops from "@/assets/images/workshops.png";
import competitions from "@/assets/images/competitions.png";
import { CONFIG } from "@/utils/constants.js";
export default {
    name: "Gallery",
    data: function initData() {
        return {
            slides: [
                {
                    image: lectures,
                    title: "Lectures",
                    description:
                        "We regularly organize open lectures for IITR junta on different tech fields we’ve been exploring like machine learning, web development, product design, game development, etc."
                },
                {
                    image: hackathons,
                    title: "SDSLabs Hackathon",
                    description:
                        "Syntax Error Campus Hackathon is where student teams participate in a 60-hour sprint of coding, coffee, designing, brainstorming, snacks and finally presenting the output."
                },
                {
                    image: workshops,
                    title: "Workshops",
                    description:
                        "We conduct hands-on workshops, which range from installing linux to even building a software from scratch, where everyone who comes can learn something new. "
                },
                {
                    image: competitions,
                    title: "Competitions",
                    description:
                        "Online competetions on ML, data science, programming, and CTFs are a great way for enthusiasts to show off some skills or learn something new in a competetive environment."
                }
            ],
            queue: 1
        };
    },
    methods: {
        carousel: function() {
            setInterval(() => {
                if (this.queue % 4 !== 0) {
                    this.queue++;
                } else this.queue = 1;
            }, 6000);
        },
        swipedetect: function(el, callback) {
            var startX = 0;
            var touchsurface = el,
                swipedir,
                startY,
                distX,
                distY,
                threshold = 30, //required min distance traveled to be considered swipe
                restraint = 300, // maximum distance allowed at the same time in perpendicular direction
                allowedTime = 300, // maximum time allowed to travel that distance
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
                    startTime = new Date().getTime(); // record time when finger first makes contact with surface
                    e.preventDefault();
                },
                false
            );

            touchsurface.addEventListener(
                "touchmove",
                function(e) {
                    e.preventDefault(); // prevent scrolling when inside DIV
                },
                false
            );

            touchsurface.addEventListener(
                "touchend",
                function(e) {
                    var touchobj = e.changedTouches[0];
                    distX = touchobj.pageX - startX; // get horizontal dist traveled by finger while in contact with surface
                    distY = touchobj.pageY - startY; // get vertical dist traveled by finger while in contact with surface
                    elapsedTime = new Date().getTime() - startTime; // get time elapsed
                    // first condition for awipe met
                    if (
                        Math.abs(distX) >= threshold &&
                        Math.abs(distY) <= restraint
                    ) {
                        // 2nd condition for horizontal swipe met
                        swipedir = distX < 0 ? "left" : "right"; // if dist traveled is negative, it indicates left swipe
                    } else if (
                        Math.abs(distY) >= threshold &&
                        Math.abs(distX) <= restraint
                    ) {
                        // 2nd condition for vertical swipe met
                        swipedir = distY < 0 ? "up" : "down"; // if dist traveled is negative, it indicates up swipe
                    }
                    handleswipe(swipedir);
                    e.preventDefault();
                },
                false
            );
        }
    },
    mounted() {
        if (window.innerWidth >= CONFIG.mobileSize) this.carousel();
        else {
            var swipearea = document.getElementsByClassName("gallery")[0];
            var vm = this;
            this.swipedetect(swipearea, function(swipedir) {
                if (swipedir == "left" || swipedir == "up") {
                    if (vm.queue < 4) vm.queue++;
                    else if (vm.queue == 4) vm.queue = 1;
                } else if (swipedir == "right" || swipedir == "down") {
                    if (vm.queue > 1) vm.queue--;
                    else if (vm.queue == 1) vm.queue = 4;
                }
            });
        }
    }
};
</script>

<style scoped lang="scss">
.textbox {
    box-shadow: 0px 6px 30px rgba(0, 0, 0, 0.07);
    border-radius: 5px;
}
</style>

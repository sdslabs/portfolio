<template>
    <div class="sister-gallery w-full">
        <div class="flex flex-col w-auto h-96 shadow-sister">
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

<template>
    <div class="w-full">
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
            <div class="mt-6 ml-10 mr-12 text-base leading-normal">
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
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."
                },
                {
                    image: pag,
                    title: "PROGRAMMING & ALGORITHMS GROUP",
                    description:
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."
                },
                {
                    image: infosec,
                    title: "INFOSEC IITR",
                    description:
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."
                }
            ],
            queue: 1
        };
    },
    methods: {
        carousel: function() {
            setInterval(() => {
                if (this.queue % 3 !== 0) {
                    this.queue++;
                } else this.queue = 1;
            }, 2000);
        }
    },
    mounted() {
        this.carousel();
    }
};
</script>

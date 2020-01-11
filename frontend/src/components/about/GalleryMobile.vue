<template>
    <div class="gallery flex flex-col w-auto">
        <carousel :per-page="1" :loop="true" :pagination-size="8">
            <slide v-for="slide in slides" v-bind:key="slide.title">
                <img
                    class="image rounded-lg"
                    v-bind:src="slide.image"
                    alt="image"
                />
                <div
                    class="textbox flex flex-col w-auto ml-6 mr-6 h-auto min-h-88 -mt-32 z-20"
                >
                    <div
                        class="font-extrabold text-2xl bg-white pl-10 pr-6 pt-10 rounded"
                    >
                        {{ slide.title }}
                    </div>
                    <div
                        class="leading-170 text-grey text-xl bg-white pt-8 pl-10 pb-8 pr-6"
                    >
                        {{ slide.description }}
                    </div>
                </div>
            </slide>
        </carousel>
    </div>
</template>

<script>
import { Carousel, Slide } from "vue-carousel";
import lectures from "@/assets/images/lectures.png";
import hackathons from "@/assets/images/hackathons.png";
import workshops from "@/assets/images/workshops.png";
import competitions from "@/assets/images/competitions.png";
import { CONFIG } from "@/utils/constants.js";
export default {
    name: "Gallery",
    components: {
        Carousel,
        Slide
    },
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
            ]
        };
    }
};
</script>

<style scoped lang="scss">
.textbox {
    box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.07);
    border-radius: 5px;
}
</style>

<template>
    <div class="sister-gallery w-full">
        <carousel :per-page="1" :loop="true" :pagination-size="8">
            <slide v-for="slide in slides" v-bind:key="slide.title">
                <div class="flex flex-col w-auto h-96 shadow-sister">
                    <div class="flex flex-row mt-8 self-center">
                        <div>
                            <img
                                class="ml-8 w-56 h-40"
                                v-bind:src="slide.image"
                            />
                        </div>
                        <div
                            class="mt-6 ml-12 mr-12 self-center leading-160 font-semibold text-1.5xl w-96"
                        >
                            {{ slide.title }}
                        </div>
                    </div>
                    <div
                        class="mt-6 ml-10 mr-12 text-xl sm:text-lg text-grey leading-normal"
                    >
                        {{ slide.description }} Visit them
                        <a
                            target="_blank"
                            class="no-underline text-darkblue"
                            :href="slide.website"
                            >here</a
                        >.
                    </div>
                </div>
            </slide>
        </carousel>
    </div>
</template>

<script>
import dsg from "@/assets/images/dsg.svg";
import pag from "@/assets/images/pag.svg";
import infosec from "@/assets/images/infosec.svg";
import { Carousel, Slide } from "vue-carousel";
export default {
    name: "SisterGallery",
    components: {
        Carousel,
        Slide
    },
    data: function initData() {
        return {
            slides: [
                {
                    website: "https://dsgiitr.com",
                    image: dsg,
                    title: "DATA SCIENCE GROUP",
                    description:
                        "As a part of SDS, this group aims at improving the culture of Data Science and Machine Learning in IIT Roorkee."
                },
                {
                    website: "https://www.facebook.com/groups/sdspag",
                    image: pag,
                    title: "PROGRAMMING & ALGORITHMS GROUP",
                    description:
                        "A bunch of competetive programming enthusiasts, PAG, frequently organizes coding lectures and contests for IITR people."
                },
                {
                    website: "https://infoseciitr.in",
                    image: infosec,
                    title: "INFOSECIITR",
                    description:
                        "InfoSecIITR is a group of information security enthusiasts. It is an open group that consists only of IITR students and alumni."
                }
            ]
        };
    }
};
</script>

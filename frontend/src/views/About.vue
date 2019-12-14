<template>
    <div class="flex flex-col pt-44 w-full">
        <div class="area_of_interest">
            <div
                class="flex flex-col-reverse md:flex-row-reverse items-center md:justify-between"
            >
                <div class="md:mr-28 md:w-220 w-full mt-16">
                    <div class="flex rounded shadow-md flex-row ml-8 mr-8 h-auto md:w-92">
                        <div class="my-8 mb-14 mx-10 w-20 h-20 md:m-8">
                            <img src="@/assets/images/interest1.png">
                        </div>
                        <div class="font-sans font-semibold self-center text-1.5xl leading-280 md:text-base align-middle md:leading-160">
                            Software Development
                        </div>
                    </div>
                    <div class="md:pl-100 md:-mt-12 mt-8">
                        <div class="flex rounded shadow-md mt-0 flex-row ml-8 mr-8 md:w-92 h-auto">
                            <div class="my-8 mb-14 mx-10 w-20 h-20 md:m-8">
                                <img src="@/assets/images/interest2.png">
                            </div>
                            <div class="font-sans font-semibold self-center text-1.5xl leading-280 md:text-base align-middle md:leading-160">
                                Information Security
                            </div>
                        </div>
                    </div>
                    <div class="md:-mt-12 mt-8">
                        <div class="flex rounded shadow-md mt-0 mr-0 flex-row ml-8 mr-8 md:w-92 h-auto">
                            <div class="my-8 mb-14 mx-10 w-20 h-20 md:m-8">
                                <img src="@/assets/images/interest3.png">
                            </div>
                            <div class="font-sans font-semibold self-center text-1.5xl leading-280 md:text-base align-middle md:leading-160">
                                Product Design
                            </div>
                        </div>
                    </div>
                    <div class="md:pl-100 md:-mt-12 mt-8">
                        <div class="flex rounded shadow-md mt-0 mr-0 flex-row ml-8 mr-8 md:w-92 h-auto">
                            <div class="my-8 mb-14 mx-10 w-20 h-20 md:m-8">
                                <img src="@/assets/images/interest4.png">
                            </div>
                            <div class="font-sans font-semibold self-center text-1.5xl leading-280 md:text-base align-middle md:leading-160">
                                Data Science
                            </div>
                        </div>
                    </div>
                    <div class="mt-6 md:-mt-12 mt-8">
                        <div class="flex rounded shadow-md mt-0 mr-0 flex-row ml-8 mr-8 md:w-92 h-auto">
                            <div class="my-8 mb-14 mx-10 w-20 h-20 md:m-8">
                                <img src="@/assets/images/interest5.png">
                            </div>
                            <div class="font-sans font-semibold self-center text-1.5xl leading-280 md:text-base align-middle md:leading-160">
                                Game Development
                            </div>
                        </div>
                    </div>
                </div>

                <div class="flex flex-col md:pl-56 ml-6">
                    <div class="text-3xl font-black md:-mt-24">Area of Interest</div>
                    <div class="text-xl md:text-base w-auto md:w-180 pt-10 font-normal text-grey leading-180 md:leading-170">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                        Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada
                        nisl. Pellentesque sagittis fringilla tempor. Pellentesque
                        sit amet augue sit amet quam feugiat porta vitae sit amet
                        ligula. Nulla posuere pellentesque metus sit amet.
                    </div>
                </div>
            </div>
        </div>

        <div class="timeline flex flex-col md:items-center md:mt-92 mt-36">
            <div
                class="flex md:flex-col md:items-center md:justify-between flex-col ml-6 md:ml-0"
            >
                <div class="text-3xl font-black">Timeline</div>
                <div class="md:text-base text-xl w-auto md:w-292 pt-10 md:mt-16 md:text-center font-normal md:font-semibold text-grey leading-180 md:leading-170">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac 
                    lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque 
                    sagittis fringilla tempor. Pellentesque sit amet augue sit amet quam 
                    feugiat porta vitae sit amet ligula.
                </div>
            </div>

            <div id="timeline_bar" class="timeline_bar flex align-bottom h-auto w-full mt-16 overflow-x-auto md:pl-64">
                <div class="timeline-bar flex flex-row-reverse flex-no-wrap py-1" v-for="timeline in timelines" v-bind:key="timeline.id">
                    <div class="timeline-box shadow-md ml-5 mr-5 self-center w-148 md:w-144 p-10">
                        <div class="text-xl md:text-base font-semibold">{{ timeline.date }}</div>
                        <div class="text-1.5xl md:text-lg text-grey-900 font-semibold pt-13">{{ timeline.title }}</div>
                        <div class="text-xl md:text-base text-grey pt-10 leading-normal">{{ timeline.description }}</div>
                    </div>
                </div>
            </div>

            <div class="scroll_icon w-auto">
                <button id="scroll_btn" class="scroll_btn self-center h-10 md:w-16 md:h-16 mt-16 md:mt-32" v-on:click="scrollFunction"><img class=" " src="@/assets/images/scroll-arrow.svg"></button>
            </div>

        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data () {
        return {
            timeline: {},
            timelines: [
                {
                    id: 6,
                    date: "March, 2018",
                    title: "Microsoft Code.Fun.do 2018",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor."
                },
                {
                    id: 5,
                    date: "February, 2018",
                    title: "LIVE Revamped",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing aenean lacinia"
                },
                {
                    id: 4,
                    date: "March, 2018",
                    title: "Microsoft Code.Fun.do 2018",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor."
                },
                {
                    id: 3,
                    date: "January, 2018",
                    title: "Inter IIT Tech Meet",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximu"
                },
                {
                    id: 2,
                    date: "February, 2018",
                    title: "CTFtime ranking",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor."
                },
                {
                    id: 1,
                    date: "December, 2018",
                    title: "XYZ",
                    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximu"
                },
            ]
        }
    },
    methods: {
        scrollFunction: function (event) {
            document.getElementById("timeline_bar").scrollLeft += 1000;
        }
    },
    mounted() {
        axios
            .get('http://0.0.0.0:8000/api/timeline')
            .then(response => {
                let timelines = {}
                for(let i = 0; i < response.data.length; i++) {
                    timelines[response.data[i]["title"]] = response.data[i]
                }
                this.timelines = Object.assign({}, this.timelines, timelines);
            })
    },
}
</script>

<style lang="scss" scoped>
.timeline_bar {
    scroll-behavior: smooth;
}
.scroll_btn:focus {
    border: none;
    outline: none;
}
.timeline_bar::-webkit-scrollbar {
    display: none;
}
.timeline_bar {
    scrollbar-width: none;
}
.timeline-bar:nth-child(odd) {
    width: 36rem;
}
.timeline-bar:nth-child(even) {
    width: 26.4rem;
}
@media only screen and (max-width: 576px) {
    .timeline-bar:nth-child(n) {
        width: 48rem;
    }
}
</style>
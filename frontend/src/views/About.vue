<template>
    <div class="flex flex-col pt-44 w-full">
        <div class="area_of_interest">
            <div
                class="flex md:flex-row-reverse items-center md:justify-between flex-col"
            >
                <div class="mr-28 w-220">
                    <div class="flex rounded shadow-md absolute flex-row w-92 h-32">
                        <div class="m-8 w-20 h-20">
                            <img src="@/assets/images/interest1.png">
                        </div>
                        <div class="font-sans font-semibold self-center text-base align-middle leading-160">
                            Software Development
                        </div>
                    </div>
                    <div class="md:pt-0 md:pl-100">
                        <div class="flex absolute rounded shadow-md mt-20 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20">
                                <img src="@/assets/images/interest2.png">
                            </div>
                            <div class="font-sans pr-10 font-semibold self-center text-base align-middle leading-160">
                                Information Security
                            </div>
                        </div>
                    </div>
                    <div class="md:pt-22">
                        <div class="flex absolute rounded shadow-md mt-20 mr-0 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20">
                                <img src="@/assets/images/interest3.png">
                            </div>
                            <div class="font-sans font-semibold self-center text-base align-middle leading-160">
                                Product Design
                            </div>
                        </div>
                    </div>
                    <div class="md:pt-20 md:pl-100">
                        <div class="flex absolute rounded shadow-md mt-20 mr-0 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20">
                                <img src="@/assets/images/interest4.png">
                            </div>
                            <div class="self-center font-sans font-semibold text-base leading-160">
                                Data Science
                            </div>
                        </div>
                    </div>
                    <div class="md:pt-22">
                        <div class="flex absolute rounded shadow-md mt-20 mr-0 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20">
                                <img src="@/assets/images/interest5.png">
                            </div>
                            <div class="font-sans font-semibold pr-8 text-base self-center leading-160">
                                Game Development
                            </div>
                        </div>
                    </div>
                </div>

                <div class="flex flex-col md:pl-56 relative w-180 h-76">
                    <div class="text-3xl font-black absolute mt-12">Area of Interest</div>
                    <div class="text-base w-180 mt-40 absolute font-semibold text-grey leading-170">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                        Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada
                        nisl. Pellentesque sagittis fringilla tempor. Pellentesque
                        sit amet augue sit amet quam feugiat porta vitae sit amet
                        ligula. Nulla posuere pellentesque metus sit amet.
                    </div>
                </div>
            </div>
        </div>

        <div class="timeline flex flex-col items-center mt-144">
            <div
                class="flex md:flex-col items-center md:justify-between flex-col"
            >
                <div class="text-3xl font-black">Timeline</div>
                <div class="text-base w-292 mt-16 text-center font-semibold text-grey leading-170">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac 
                    lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque 
                    sagittis fringilla tempor. Pellentesque sit amet augue sit amet quam 
                    feugiat porta vitae sit amet ligula.
                </div>
            </div>

            <div id="timeline_bar" class="timeline_bar flex align-bottom h-100 w-full mt-32 overflow-x-auto pl-64">
                <div id="timeline-bar" class="timeline-bar flex flex-row-reverse flex-no-wrap" v-for="timeline in timelines" v-bind:key="timeline.id">
                    <div class="timeline-box shadow-md ml-5 mr-5 self-center w-144 p-10">
                        <div class="text-base font-semibold">{{ timeline.date }}</div>
                        <div class="text-lg text-grey-900 font-semibold pt-13">{{ timeline.title }}</div>
                        <div class="text-base text-grey pt-10 leading-normal">{{ timeline.description }}</div>
                    </div>
                </div>
            </div>

            <div class="scroll_icon">
                <button id="scroll_btn" class="scroll_btn w-16 h-16 mt-32" v-on:click="scrollFunction"><img class=" " src="@/assets/images/scroll-arrow.svg"></button>
            </div>

        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
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
    }
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
</style>
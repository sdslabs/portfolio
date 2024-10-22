<template>
    <div class="sticky">
        <vue-marquee-slider id="marquee-slider-loop" :speed="5000" :width="450">
            <span>
                Registrations for
                <span style="color: #01CFFF; font-weight: 600;"
                    ><a
                        href="https://hackathon.sdslabs.co/"
                        target="_blank"
                        style="text-decoration: none; color: #01CFFF"
                        >Syntax Error 11</a
                    >
                </span>
                are live !
            </span>
        </vue-marquee-slider>
    </div>
</template>

<script>
import Vue from "vue";
import VueMarqueeSlider from "vue-marquee-slider";

Vue.use(VueMarqueeSlider);

export default {
    data() {
        return {};
    }
};
</script>

<style>
.sticky {
    position: sticky;
    top: 0;
    z-index: 1000; /* Ensure it stays on top of other content */
    background-color: #000000; /* Background color to match the marquee */
}
#marquee-slider,
#marquee-slider-loop {
    padding: 12px 0;
    font-size: 24px; /* Adjust font size as needed */
    color: #ffffff; /* Default text color */
    white-space: nowrap; /* Prevent text from wrapping */
    background: #000000;
}
</style>

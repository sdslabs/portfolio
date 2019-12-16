<template>
    <div class="w-full pt-38 overflow-x-hidden">
        <div class="flex flex-col md:flex-row">
            <div class="md:pt-72">
                <img class="h-32 -ml-32 md:w-188 md:h-44 md:ml-0" src="@/assets/images/error-left.svg"/>
            </div>
            <div class="">
                <img class=" hidden md:block md:w-212 md:h-140" src="@/assets/images/404.svg">
            </div>
            <div class="pt-14 flex justify-center">
                <img class=" md:hidden" src="@/assets/images/404.png">
            </div>
            <div class="pt-12 md:pt-72">
                <img class=" h-32 ml-64 md:ml-0 md:w-216 md:h-44" src="@/assets/images/error-right.svg"/>
            </div>
        </div>
        <div class=" pt-48 text-lg md:pt-20 font-semibold leading-normal md:text-2xl text-center">
            Something went wrong... please try again
        </div>
        <div class="text-center">
            <button class="w-96 h-26 md:w-72 md:h-20 bg-error mt-16 md:mt-20 p-4 leading-170 text-lg md:text-base font-extrabold text-white" onclick="location.href = '/';">
                Go to Home
                <span class=" md:inline-block md:h-full md:align-middle">
                    <img class="pl-8 -mb-2" src="@/assets/images/button-arrow.svg">
                </span>
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "Error404",
}
</script>
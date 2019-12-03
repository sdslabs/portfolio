<template>
    <div class="w-full pt-38">
        <div class="flex flex-row justify-center">
            <div class="pt-72">
                <img class="w-188 h-44" src="@/assets/images/error-left.svg"/>
            </div>
            <div class="">
                <img class="w-212 h-140" src="@/assets/images/404.svg">
            </div>
            <div class="pt-72">
                <img class="w-216 h-44" src="@/assets/images/error-right.svg"/>
            </div>
        </div>
        <div class=" pt-20 font-semibold leading-normal text-2xl text-center">
            Something went wrong... please try again
        </div>
        <div class="text-center">
            <button class="w-72 h-20 bg-error mt-20 p-4 leading-170 text-base font-extrabold text-white" onclick="">
                Go to Home
                <span class="self-center">
                    <img class="pl-8 -mb-2" src="@/assets/images/button-arrow.svg">
                </span>
            </button>
        </div>
    </div>
</template>
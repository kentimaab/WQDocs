---
hide:
- toc
---


Theme Builder
====

Here the user can create their custom themes. If your looking for a guide to import your custom theme into WideQuick can be found [here](../mod/modules/Core/themes.md) 

## Generate Theme
<iframe src="https://material-foundation.github.io/material-theme-builder/" style="width: 100%; height: 800px; border: solid;"></iframe>


## Parse Theme into WideQuick format


<div style="display: flex; gap: 20px;" markdown>

<div class="container">
<p>Step 1: Select the Themes.kdat file from your project</p>
<label for="wqFile" class="headerLabel">
<div class="header">
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g id="SVGRepo_bgCarrier" stroke-width="0"></g>
<g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
<g id="SVGRepo_iconCarrier">
  <path
    d="M7 10V9C7 6.23858 9.23858 4 12 4C14.7614 4 17 6.23858 17 9V10C19.2091 10 21 11.7909 21 14C21 15.4806 20.1956 16.8084 19 17.5M7 10C4.79086 10 3 11.7909 3 14C3 15.4806 3.8044 16.8084 5 17.5M7 10C7.43285 10 7.84965 10.0688 8.24006 10.1959M12 12V21M12 12L15 15M12 12L9 15"
    stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
</g>
</svg>
<p>Browse Themes.kdat file to use!</p>
</div>
</label>
<input type="file" id="wqFile" accept=".kdat">
<p id="wqFileNameDisplay" style="margin-top: 10px; font-size: 14px; "></p>
</div>

<div class="container">
<p>Step 2: Select the Colors.xml file from the theme you created</p>
<label for="themeFile" class="headerLabel">
<div class="header">
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g id="SVGRepo_bgCarrier" stroke-width="0"></g>
<g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
<g id="SVGRepo_iconCarrier">
<path
  d="M7 10V9C7 6.23858 9.23858 4 12 4C14.7614 4 17 6.23858 17 9V10C19.2091 10 21 11.7909 21 14C21 15.4806 20.1956 16.8084 19 17.5M7 10C4.79086 10 3 11.7909 3 14C3 15.4806 3.8044 16.8084 5 17.5M7 10C7.43285 10 7.84965 10.0688 8.24006 10.1959M12 12V21M12 12L15 15M12 12L9 15"
  stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
</g>
</svg>
<p>Browse Color.xml file to use!</p>
</div>
</label>
<input type="file" id="themeFile" accept=".xml">
<p id="themeFileNameDisplay" style="margin-top: 10px; font-size: 14px; "></p>
</div>
</div>
<button id="modifyBtn">Merge new theme into existing themes file </button>

<a id="downloadLink" download ></a>    




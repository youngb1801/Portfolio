<!-- PROJECT SHIELDS -->
<!--
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/youngb1801/Portfolio/tree/main/Timeseries_Analysis">
    <img src="images/sales.png" alt="Logo" width="120" height="100">
  </a>

  <h3 align="center">Time Series Analysis</h3>

  <p align="center">
    Can sales be forecast based on past data?
    <br />
    <a href="https://github.com/youngb1801/Portfolio/tree/main/Timeseries_Analysis"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/youngb1801/Portfolio/tree/main/Timeseries_Analysis">View Demo</a>
    ·
    <a href="https://github.com/youngb1801/Portfolio/issues">Report Bug</a>
    ·
    <a href="https://github.com/youngb1801/Portfolio/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The goal of this project was to forecast the next 7 days after the series data ended.

The hypothesis, can a naive baseline model perform better than an autoregressive integrated moving average, ARIMA?, the hypothesis was disproved and the ARIMA model outperformed the baseline.

### Built With

* [Python 3](https://www.python.org)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Data can be obtained from Kaggle [Womens Ecommerce Clothing Reviews](https://www.kaggle.com/nicapotato/womens-ecommerce-clothing-reviews)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/youngb1801/Portfolio.git
   ```
2. Install the following packages

  ```sh
  pip install pandas
  ```

  * [Pandas](https://pandas.pydata.org)
  * [Scikit-Learn](https://scikit-learn.org/stable/#)
  * [Numpy](https://numpy.org)
  * [Matplotlib](https://matplotlib.org/stable/index.html)
  * [Seaborn](https://seaborn.pydata.org)
  * [Statsmodels](https://www.statsmodels.org/stable/index.html)
  * [Dateutil](https://dateutil.readthedocs.io/en/stable/)

<!-- USAGE EXAMPLES -->
## Usage

Sales forecasting is an important aspect of determining if the company is meeting their goals, set budgets and determine if sales promotions are needed.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/youngb1801/Portfolio/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Bret Young - bayoung1801@gmail.com

Project Link: [https://github.com/youngb1801/Portfolio/tree/main/Timeseries_Analysis](https://github.com/youngb1801/Portfolio/tree/main/Timeseries_Analysis)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/youngb1801/Portfolio.svg?style=for-the-badge
[contributors-url]: https://github.com/youngb1801/Portfolio/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/youngb1801/Portfolio.svg?style=for-the-badge
[forks-url]: https://github.com/youngb1801/Portfolio/network/members
[stars-shield]: https://img.shields.io/github/stars/youngb1801/Portfolio.svg?style=for-the-badge
[stars-url]: https://github.com/youngb1801/Portfolio/stargazers
[issues-shield]: https://img.shields.io/github/issues/youngb1801/Portfolio.svg?style=for-the-badge
[issues-url]: https://github.com/youngb1801/Portfolio/issues
[license-shield]: https://img.shields.io/github/license/youngb1801/Portfolio.svg?style=for-the-badge
[license-url]: https://github.com/youngb1801/Portfolio/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/bret-young-4b5b0ba9/

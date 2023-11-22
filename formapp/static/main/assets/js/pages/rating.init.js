if (document.querySelector("#rater-step-1")) {
    starRatingStep1 = raterJs({
        starSize: 22,
        rating: 2,
        element: document.querySelector("#rater-step-1"),
        rateCallback: function (e, t) {
            this.setRating(e);
            t();
        }
    });
}

if (document.querySelector("#rater-step-2")) {
    starRatingStep2 = raterJs({
        starSize: 22,
        rating: 2,
        element: document.querySelector("#rater-step-2"),
        rateCallback: function (e, t) {
            this.setRating(e);
            t();
        }
    });
}

if (document.querySelector("#rater-step-3")) {
    starRatingStep3 = raterJs({
        starSize: 22,
        rating: 2,
        element: document.querySelector("#rater-step-3"),
        rateCallback: function (e, t) {
            this.setRating(e);
            t();
        }
    });
}

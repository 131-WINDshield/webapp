(() => {

    jQuery("#searchForm").submit(function(e) {
        // e.preventDefault();
        var category = jQuery("#searchType").val();
        var value = jQuery("#searchValue").val();

        jQuery.ajax({
            type: "POST",
            url: "/search",
            async: false,
            data: {
                'type': category,
                'searched': value,
            },
            success: (response) => {
                // console.log(response);
            }
        })
    })

})();
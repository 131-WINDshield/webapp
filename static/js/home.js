(() => {

    jQuery("#carForm").submit(function(e) {
        e.preventDefault()
        var name = jQuery("#carName").val();
        var brand = jQuery("#carBrand").val();
        var miles = jQuery("#carMileage").val();
        var mpg = jQuery("#carMpg").val();
        console.log(name, brand, miles, mpg);

        jQuery.ajax({
            type: "POST",
            url: "/",
            async: false,
            data: {
                'name': name,
                'brand': brand,
                'mileage': miles,
                'mpg': mpg
            },
            success: (response) => {
                console.log(response);
                // document.location.href = "/print"
            },
            error: function(xhr, status, error) {
                console.log('error');
            },
            timeout: 3000 // 3 seconds
        })
    })

})();
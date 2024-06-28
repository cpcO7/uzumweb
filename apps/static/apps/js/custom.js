 function formatPhoneNumber(input) {
    let value = input.value.replace(/\D/g, ''); // Remove all non-numeric characters

    // Ensure the prefix is always "+998 "
    if (!value.startsWith("998")) {
        value = "998" + value;
    }

    // Format the phone number
    let formattedValue = "+998 ";
    if (value.length > 3) {
        formattedValue += value.substring(3, 5);
    }
    if (value.length > 5) {
        formattedValue += " " + value.substring(5, 8);
    }
    if (value.length > 8) {
        formattedValue += "-" + value.substring(8, 10);
    }
    if (value.length > 10) {
        formattedValue += "-" + value.substring(10, 12);
    }
        input.value = formattedValue;
}



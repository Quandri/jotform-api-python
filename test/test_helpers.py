import pytest
import object_file
import helpers


@pytest.fixture
def jotform_api_res_driver_addition():
    "Load a sample response from JotForm API from Driver Addition folder"
    jet_form_response = object_file.get_object_from_file(
        object_num=1,
        object_name="test/data/jotform_api_response_driver_addition.json",
    )
    return jet_form_response


@pytest.fixture
def reformatted_driver_addition():
    """Load a sample expected reformatted data for the driver addition"""
    reformatted_response = object_file.get_object_from_file(
        object_num=1,
        object_name="test/data/reformatted_driver_addition_list.json",
    )

    return reformatted_response


def test_reformat_submission_list(
    jotform_api_res_driver_addition, reformatted_driver_addition
):
    """Test reformatting the data"""
    assert (
        helpers.reformat_submission_list(jotform_api_res_driver_addition)
        == reformatted_driver_addition
    )


def test_create_date_from_dict():
    """Test create a date string from given dictionary"""
    input_one = {"month": 12, "day": 23, "year": 1999}
    input_two = "{'month: 12, 'day': 23, 'year': 1999}"

    assert helpers.create_date_from_dict(input_one) == "12/23/1999"

    # Check if it will raise TypeError
    with pytest.raises(TypeError):
        helpers.create_date_from_dict(input_two)

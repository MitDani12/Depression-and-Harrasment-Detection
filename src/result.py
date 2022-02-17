def get_result(depression_prediction, harassment_prediction):

    result_flag = depression_prediction and harassment_prediction

    if result_flag:
        return 'Both'
    else:
        if depression_prediction == 1 and harassment_prediction == 0:
            return 'Depression'
        elif depression_prediction == 0 and harassment_prediction == 1:
            return 'Harassment'
        else:
            return 'Neither'

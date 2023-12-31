import json, typing

########################
# I/O HELPER FUNCTIONS #
########################
def readRequest() -> typing.Any:
    '''
    readRequest will return the Rising Cloud request made to the worker.
    By default, this returns a dict. This reads from the request filepath, (by
    default this is "request.json" which is created by Rising Cloud when the
    worker receives a request) and outputs loaded and transformed data.
    '''

    with open("./request.json", "r") as f:
        request = json.load(f)

        # Perform any transformations of the input data here. Common
        # transformations might be to convert to another data type or to use
        # the request to go fetch data through a request.

        return request

def writeResponse(response: typing.Any):
    '''
    writeResponse takes any json-serializable object and writes the serialized
    string to the response filepath. When running on the Rising Cloud platform,
    this filepath should always be "response.json" as that is where Rising Cloud
    automatically looks for a response after the main function terminates.
    '''

    # Perform any transformations to output data here.
    
    with open("./response.json", "w") as f:
        json.dump(response, f)


################
# MAIN PROCESS #
################
if __name__ == "__main__":

    # We first read the request from "request.json". If you'd like to do any
    # pre-processing to the request, edit the readRequest() function and return
    # with the appropriate processed data type.
    request = readRequest()

    # To process the request with an arbitrary function, import the function
    # and replace this line with `response = arbitraryFunctionName(request)`.
    response = request

    # Demonstration of logs that will be captured by the Rising Cloud worker.
    # These logs will be reported in the app's /jobs page under the "Std Error"
    # and "Std Out" respectively. They serve no purpose other than to show
    # how to implement logs and how they will be captured by Rising Cloud.
    import sys
    print("This is a demo log to stderr", file=sys.stderr)
    print("This is a demo log to stdout")

    # Serialize and write out the response to "response.json". If you'd like to
    # do any post-processing to the response, edit the writeResponse()
    # function to take in the unprocessed datatype and transform it there.
    writeResponse(response)

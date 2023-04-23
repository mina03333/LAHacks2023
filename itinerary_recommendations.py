import cohere
co = cohere.Client('3oLfmlBPNNCZBWB008008nFdhJ8Z6rDPCnwRDNyo')


def itinerary(info):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=f'Using this information, create an itinerary for the day:{info}. Format the results as:(time) - (name)\n\tPrice Range: (price range)\n\tLocation: (location)\n\tServices: (services)',
        max_tokens=1432,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))

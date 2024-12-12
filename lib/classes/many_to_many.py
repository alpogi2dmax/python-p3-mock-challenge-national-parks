class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and hasattr(self, '_name') == False:
            self._name = name


    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        unique_visitors = []
        for trip in Trip.all:
            if trip.visitor not in unique_visitors and trip.national_park == self:
                unique_visitors.append(trip.visitor)
        return unique_visitors
    
    def total_visits(self):
        if len(self.trips()) > 0:
            return len(self.trips())
        else:
            return 0
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in Trip.all if trip.national_park == self]
        return max(set(visitors), key = visitors.count)


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
    
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park


class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        unique_national_parks = []
        for trip in Trip.all:
            if trip.national_park not in unique_national_parks and trip.visitor == self:
                unique_national_parks.append(trip.national_park)
        return unique_national_parks
    
    def total_visits_at_park(self, park):
        visited_park = []
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park == park:
                visited_park.append(self)
        if len(visited_park) > 0:
            return len(visited_park)
        else:
            return 0
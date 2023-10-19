name = []
description = []
registration = []
for i in range(len(name)):
    print(rf'''<li class="accordion-item">
											<a class="accordion-title" href="javascript:void(0)">
												<!-- <div class="author">
													<img src="assets/img/author1.jpg" data-toggle="tooltip" data-placement="top" title="Battle of Bands" alt="image">
												</div> -->
												
												<div class="schedule-info">
													<h3>{name[i]}</h3>
                                                    <ul>
														<li><i class="icofont-wall-clock"></i>{description[i]}</li>
													</ul>
												</div>
											</a>
											
											<div class="accordion-content">
												<p>{registration[i]}</p>

												<div class="row h-100 align-items-center">
													<div class="col-lg-6">
														<div class="location">
															
														</div>
													</div>

													<div class="col-lg-6 text-end">
														<a href="sci-tech/artpark.html" class="btn btn-primary">View Details</a>
													</div>
												</div>
											</div>
										</li>''')

